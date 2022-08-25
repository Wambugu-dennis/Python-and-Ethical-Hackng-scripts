#!/usr/bin/env python

# created by Wambugu
# 26-08-2022

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()


scan("192.168.100.1/24")
