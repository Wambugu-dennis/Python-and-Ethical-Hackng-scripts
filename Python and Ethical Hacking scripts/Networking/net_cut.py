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

import netfilterqueue


def process_packet(packet):
    print(packet)
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
