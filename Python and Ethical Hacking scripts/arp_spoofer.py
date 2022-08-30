#!/usr/bin/env python

# created by Wambugu
# 30-08-2022

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.100.152", hwdst="92:9a:4a:07:d4:17", psrc="192.168.100.1")
print(packet.show())
print(packet.summary())

#  this is a test
