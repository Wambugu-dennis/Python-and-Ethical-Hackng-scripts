#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


# created by Wambugu
# 01-09-2022

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet, filter="port 80")


def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet.show())


sniff("wlo1")
