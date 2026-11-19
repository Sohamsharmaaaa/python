# Write a Python program that accepts a target host and a port range from the user, validates both, scans
# using python-nmap and writes the report (host, port, state, service) to a file.

import nmap
import socket

# Get and validate the host
host = input("Enter target host (IP or name): ")
try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Invalid host")
    exit()

port_range = input("Enter port range (e.g. 20-80): ")
try:
    start, end = port_range.split("-")
    start, end = int(start), int(end)
    if not (1 <= start <= end <= 65535):
        raise ValueError
except ValueError:
    print("Invalid port range. Use format start-end, values 1-65535")
    exit()

# Scan
scanner = nmap.PortScanner()
print("Scanning", ip, "...")
scanner.scan(ip, f"{start}-{end}")

# Write report
with open("scan_report.txt", "w") as f:
    f.write("Host\tPort\tState\tService\n")
    for h in scanner.all_hosts():
        for port in scanner[h]["tcp"]:
            state = scanner[h]["tcp"][port]["state"]
            service = scanner[h]["tcp"][port]["name"]
            line = f"{h}\t{port}\t{state}\t{service}"
            print(line)
            f.write(line + "\n")

print("Report saved to scan_report.txt")
