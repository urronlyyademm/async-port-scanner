#!/usr/bin/env python3
"""
Async TCP Port Scanner & Banner Grabber
A fast, asynchronous port scanner leveraging Python's asyncio module.
"""

import argparse
import asyncio
import socket
from datetime import datetime


async def grab_banner(reader: asyncio.StreamReader) -> str:
    """Attempt to read service banner from an open socket."""
    try:
        data = await asyncio.wait_for(reader.read(1024), timeout=1.5)
        return data.decode("utf-8", errors="ignore").strip()
    except (asyncio.TimeoutError, Exception):
        return "No banner"


async def scan_port(target_ip: str, port: int, timeout: float, semaphore: asyncio.Semaphore) -> tuple[int, bool, str]:
    """Scan a single TCP port using asyncio socket connection."""
    async with semaphore:
        try:
            conn = asyncio.open_connection(target_ip, port)
            reader, writer = await asyncio.wait_for(conn, timeout=timeout)
            banner = await grab_banner(reader)
            writer.close()
            await writer.wait_closed()
            return port, True, banner
        except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
            return port, False, ""


def parse_ports(port_input: str) -> list[int]:
    """Parse comma-separated ports and ranges (e.g., '21-25,80,443')."""
    ports = set()
    parts = port_input.split(",")
    for part in parts:
        part = part.strip()
        if "-" in part:
            start, end = map(int, part.split("-"))
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))
    return sorted(list(ports))


async def run_scanner(target: str, ports: list[int], timeout: float, concurrency: int) -> None:
    """Orchestrate concurrent port scanning tasks."""
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Error: Could not resolve hostname '{target}'")
        return

    print(f"\n[*] Starting scan on target: {target} ({target_ip})")
    print(f"[*] Scanning {len(ports)} ports with concurrency={concurrency} and timeout={timeout}s")
    print(f"[*] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 65)

    semaphore = asyncio.Semaphore(concurrency)
    tasks = [scan_port(target_ip, port, timeout, semaphore) for port in ports]

    open_ports = 0
    results = await asyncio.gather(*tasks)

    for port, is_open, banner in results:
        if is_open:
            open_ports += 1
            banner_info = f" | Banner: {banner}" if banner and banner != "No banner" else ""
            print(f"[+] Port {port:<5} [OPEN]{banner_info}")

    print("-" * 65)
    print(f"[*] Scan finished. Found {open_ports} open port(s).\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fast Asynchronous TCP Port Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("target", help="Target hostname or IP address (e.g., scanme.nmap.org or 127.0.0.1)")
    parser.add_argument(
        "-p",
        "--ports",
        default="21-25,53,80,110,143,443,3306,8080",
        help="Ports to scan (e.g., '80,443' or '1-1000'). Default: Common service ports",
    )
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Connection timeout in seconds (default: 1.0)")
    parser.add_argument("-c", "--concurrency", type=int, default=200, help="Max concurrent connections (default: 200)")

    args = parser.parse_args()

    try:
        ports = parse_ports(args.ports)
    except ValueError:
        print("[!] Invalid port format. Example format: '22,80,443' or '1-1024'")
        return

    asyncio.run(run_scanner(args.target, ports, args.timeout, args.concurrency))


if __name__ == "__main__":
    main()
