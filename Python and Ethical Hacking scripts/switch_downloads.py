#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    my_packet = scapy.IP(packet.get_payload())
    if my_packet.haslayer(scapy.Raw):
        if my_packet[scapy.TCP].dport == 80:
            print("[+] HTTP Request...")
            if ".exe" in my_packet[scapy.Raw].load:
                print("[+] .exe Request file requested")

            print(my_packet.show())
        elif my_packet[scapy.TCP].sport == 80:
            print("[+] HTTP Response")
            print(my_packet.show())

    packt.accept()


queue = netfilterqueue.NetfiletrQueue()
queue.bind(0, process_packet)
queue.run()
