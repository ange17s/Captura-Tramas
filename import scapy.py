import scapy.all as scapy

ip = "192.168.43.1"
print(scapy.arping(ip))

arp = scapy.ARP(pdst = ip)

print(arp.show())