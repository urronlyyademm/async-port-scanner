
# ⚡ Async Port Scanner

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Platform: Cross-Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg?style=flat-square)](#)

A high-performance, asynchronous TCP port scanner and service banner grabber engineered with Python's native `asyncio` and `socket` libraries. Designed for rapid network reconnaissance and security audits without external heavy dependencies.

---

## ✨ Features

- ⚡ **Asynchronous Concurrency:** Leverages `asyncio` and semaphores to scan hundreds of ports concurrently.
- 🎯 **Flexible Target & Port Ranges:** Supports single ports (`80,443`), ranges (`1-1024`), or mixed lists (`22,80,8000-8080`).
- 🔍 **Service Banner Grabbing:** Intercepts response banners from responsive ports to assist in service identification.
- ⏱️ **Configurable Parameters:** Adjustable socket timeouts and concurrency limits.
- 📦 **Zero External Dependencies:** Built purely using the Python standard library.

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
      git clone [https://github.com/urronlyyademm/async-port-scanner.git](https://github.com/urronlyyademm/async-port-scanner.git)
      cd async-port-scanner



2. **Ensure Python 3.10+ is installed:**
```bash
python3 --version

```



---

## 💻 Usage & Examples

### Basic Scan (Default Top Ports)

```bash
python3 scanner.py scanme.nmap.org

```

### Scan Specific Port Range with Custom Concurrency

```bash
python3 scanner.py 127.0.0.1 -p 1-1000 -c 300 -t 0.8

```

### Scan Comma-Separated Ports

```bash
python3 scanner.py target.local -p 21,22,80,443,3306,8080

```

---

## 📋 Command-Line Arguments

| Flag | Argument | Default | Description |
| --- | --- | --- | --- |
| `target` | `STRING` | *Required* | Target IP address or hostname |
| `-p`, `--ports` | `STRING` | `Common ports` | Ports/ranges to scan (e.g. `80,443` or `1-1000`) |
| `-t`, `--timeout` | `FLOAT` | `1.0` | Socket connection timeout in seconds |
| `-c`, `--concurrency` | `INT` | `200` | Maximum simultaneous open connections |

---

## 🛡️ Disclaimer

This tool is created for educational purposes, authorized security auditing, and local network diagnostics only. Scanning targets without prior mutual consent is strictly illegal. The author assumes no liability for misuse.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

