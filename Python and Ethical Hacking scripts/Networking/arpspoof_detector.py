#!/usr/bin/env python
# -*- encoding: utf-8 -*-

##############################################################################
#                                                                            #
#                                 py & EH                                    #
#                                                                            #
##############################################################################

# Disclaimer: Do Not Use this program for illegal purposes ;)
import netfilterqueue
import scapy.all as scapy
import re

import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  # get IPs of clients from arp broadcast request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # send arp request to the broadcast address
    arp_request_broadcast = broadcast / arp_request
    # capture answered result packets in a list, set a time to end search and less verbose result
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet, filter="port 80")


def sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print("[+] Your network is under attack!! ")
        except IndexError:
            pass


sniff("[enter your interface here!!]")
