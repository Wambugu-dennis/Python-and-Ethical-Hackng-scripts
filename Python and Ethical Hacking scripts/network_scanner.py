#!/usr/bin/env python

# created by Wambugu
# 26-08-2022

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # get IPs of clients from arp broadcast request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # send arp request to the broadcast address
    arp_request_broadcast = broadcast / arp_request
    # capture answered result packets in a list, set a time to end search and less verbose result
    answered_lst = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\t\tMAC ADDRESS\n-------------------------------------------------------------------")

    # loop through function to read all elements from answered list and display result
    for element in answered_lst:
        print(element[1].psrc + "\t\t\t" + element[1].hwsrc)  # print result IP and MAC addresses in a table
        print("-------------------------------------------------------------------")


scan("192.168.1.1/24")
