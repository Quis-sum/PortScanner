# PortScanner

A lightweight, dependency-free port scanner built in Python. Supports targeted and full-range TCP scans with automatic hostname resolution and structured scan summaries. Designed as a practical demonstration of low-level network programming using Python's `socket` module.

---

## Features

- Scan a **single port**, **multiple ports**, or **all 65,535 ports**
- Accepts both **IP addresses** and **hostnames** as targets
- Automatic **hostname resolution** with graceful fallback to `127.0.0.1`
- Structured **scan summary** including target, port range, start time, end time, and open port count
- Handles keyboard interrupts and connection errors cleanly

---

## Requirements

- Python 3.x
- No external dependencies — uses only the Python standard library (`socket`, `sys`, `re`, `time`, `datetime`)

---

## Usage

### Syntax

```bash
python shittyPortScanner.py [TARGET] [PORT(S)]
```

All arguments are optional. If omitted, the scanner will prompt for them interactively.

---

### Examples

**Interactive mode:**
```bash
python shittyPortScanner.py
```

**Default scan — ports 1 to 1023:**
```bash
python shittyPortScanner.py 192.168.1.1
```
*Press ENTER when prompted for ports to use the default range.*

**Scan specific ports:**
```bash
python shittyPortScanner.py 192.168.1.1 22 80 443
```

**Full port scan — ports 1 to 65535:**
```bash
python shittyPortScanner.py 192.168.1.1 -p-
```

**Scan using a hostname:**
```bash
python shittyPortScanner.py example.com 80 443
```

---

## Sample Output

```
============================================================
[+] TARGET:               192.168.1.1
[+] PORT(S):              range(1, 1024)
[+] TIME STARTED:         2026-03-15 10:22:01.483921
============================================================
Scanning 192.168.1.1...
This might take a while...
Port 22 is open
Port 80 is open
============================================================
[+] TIME FINISHED:        2026-03-15 10:22:14.201384
[+] NO of OPEN PORT(S):   2
============================================================
```

---

## Technical Notes

- Each connection attempt has a **1-second timeout**. Scanning the full port range may take several minutes depending on network conditions.
- If hostname resolution fails, the scanner defaults to `127.0.0.1` (localhost) and continues.
- Only **TCP** connections are tested (`SOCK_STREAM`). UDP ports are out of scope.

---

## Disclaimer

This tool is intended for **educational purposes and authorised use only**. Scanning systems without explicit permission may be illegal in your jurisdiction. Always ensure you have the right to scan any target before running this tool.

---

## Author

[Quis-sum](https://github.com/Quis-sum)
