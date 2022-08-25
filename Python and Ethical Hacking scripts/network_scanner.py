#!/usr/bin/env python

# created by Wambugu Dennis
# 26-08-2022

import scapy.all as copy
import scapy.layers.l2


def scan(ip):
    scapy.layers.l2.arping(ip)


scan("192.168.1.1/24")
