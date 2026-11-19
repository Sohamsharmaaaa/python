# Write a Python program using Scapy to send a TCP SYN packet to ports 20-30 of 127.0.0.1 and report which ports
# are open (SYN-ACK received).
from scapy.all import IP, TCP, sr1, send

target = "127.0.0.1"

for port in range(20, 31):
    # Send SYN packet
    packet = IP(dst=target) / TCP(dport=port, flags="S")
    reply = sr1(packet, timeout=1, verbose=0)

    if reply is None:
        print(f"Port {port}: No response (filtered)")
    elif reply.haslayer(TCP) and reply[TCP].flags == 0x12:
        # 0x12 = SYN-ACK
        print(f"Port {port}: OPEN")
        # Send RST to close the half-open connection
        send(IP(dst=target) / TCP(dport=port, flags="R"), verbose=0)
    else:
        print(f"Port {port}: Closed")

"""
To run this script, open another terminal and start python server listen on port no. 25
python -m http.server 25

"""
