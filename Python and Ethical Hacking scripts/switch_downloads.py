#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    my_packet = scapy.IP(packet.get_payload())
    if my_packet.haslayer(scapy.DNSRR):

        packt.accept()


queue = netfilterqueue.NetfiletrQueue()
queue.bind(0), process_packet)
queue.run()