# Write a Python program using Scapy to create an ICMP echo request packet for 127.0.0.1, display its layers using show()  and send it.

from scapy.all import IP, ICMP, send, sr1

# Build the ICMP echo request (ping) packet for localhost
packet = IP(dst="127.0.0.1") / ICMP()

# Display the packet's layers and field values
print("=== Packet layers ===")
packet.show()

# Send the packet (layer 3, no reply handling)
print("\n=== Sending packet ===")
send(packet)
