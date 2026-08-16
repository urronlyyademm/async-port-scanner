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
      cd async-port-scannee
