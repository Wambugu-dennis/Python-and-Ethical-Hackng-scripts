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
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-I", "--iprange", dest="ip", help="target ip address / ip address range to scan")
    options = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify an ip address range, use --help for more info.")
    elif options.ip:
        return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # get IPs of clients from arp broadcast request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # send arp request to the broadcast address
    arp_request_broadcast = broadcast / arp_request
    # capture answered result packets in a list, set a time to end search and less verbose result
    answered_lst = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []  # list to contain all the dictionaries
    # loop through function to read all elements from answered list and display result
    for element in answered_lst:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)  # append dictionaries containing data for each client to main list
    return clients_list


def print_result(results_list):
    print("IP\t\t\t\tMAC ADDRESS\n-------------------------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t\t" + client["mac"])  # print result IP and MAC addresses in a table
        print("-------------------------------------------------------------------")


options = get_arguments()
scan_result = scan(options.ip)
print_result(scan_result)
