"""
Build a tool to analyze authentication logs. Each line has the format:
        2026-10-27 09:15:32,192.168.1.10,LOGIN_FAILED,admin
Write a python script that reads a log file and counts failed login attempts per IP address.
1. Handle FileNotFoundError and PermissionError separately, with different messages.
2. Malformed lines (wrong number of fields, invalid IP format, unparseable timestamp) must not crash the program.
   Log them to a separate list with the line number and the reason, then continue processing.
3. Use ipaddress.ip_address() to validate IPs and catch the exception it raises.
4. Use the with statement for file handling.
5. At the end, print the offending IPs and a summary of how many lines were skipped.
"""

"""
sample_auth.log file 

2026-10-27 09:15:32,192.168.1.10,LOGIN_FAILED,admin
2026-10-27 09:15:40,192.168.1.10,LOGIN_FAILED,root
2026-10-27 09:16:01,10.0.0.5,LOGIN_OK,akash
2026-10-27 09:16:15,10.0.0.99,LOGIN_FAILED,sarika
2026-10-27 09:17:00,999.1.1.1,LOGIN_FAILED,admin
2026-10-27 25:99:00,10.0.0.99,LOGIN_FAILED,sarika
only,two,fields
2026-10-27 09:18:00,10.0.0.99,LOGIN_FAILED,sameer

"""

import ipaddress
import sys
from collections import Counter
from datetime import datetime


# Return (timestamp, ip, event, user) or raise ValueError with a error message.
def parse_line(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 4:
        raise ValueError(f"expected 4 fields, got {len(parts)}")
    ts, ip, event, user = parts
    try:
        datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(f"unparseable timestamp '{ts}'")
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise ValueError(f"invalid IP address '{ip}'")
    return ts, ip, event, user


def analyze(filename):
    failed = Counter()
    skipped = []  # contains tuple (line_number, reason)
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    _, ip, event, _ = parse_line(line)
                except ValueError as e:
                    skipped.append((lineno, str(e)))
                    continue
                if event == "LOGIN_FAILED":
                    failed[ip] += 1
    except FileNotFoundError:
        print(f"Error: file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: no permission to read '{filename}'.")
        return
    except UnicodeDecodeError as e:
        print(f"Error: file is not valid UTF-8 ({e.reason}).")
        return

    print("Offending IPs:")
    for ip, count in failed.items():
        print(f"{ip} ----> {count} failed attempts")
    print(f"\nSkipped lines are: {len(skipped)}")
    for lineno, reason in skipped:
        print(f"line {lineno}: {reason}")


# main block ---- command line argument
analyze(sys.argv[1] if len(sys.argv) > 1 else "auth.log")

""" 
execute as follows on $ prompt
$python Ass2_exception_log_analyzer.py sample_auth.log
"""
