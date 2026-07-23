from scapy.all import ICMP, IP, sr, sr1, ARP, Ether
import socket

def arp_scan(ip_range):
    """
    Perform an ARP scan on the given IP range.
    """
    ans, unans = sr1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=2, verbose=0)
    for snd, rcv in ans:
        if rcv is not None:
            print(f"IP: {rcv.sprintf(r"%ARP.psrc%")} MAC: {rcv.sprintf(r"%Ether.src%")}")

def ping_scan(ip_range):
    """
    Perform a ping scan on the given IP range.
    """
    ans, unans = sr1(IP(dst=ip_range)/ICMP(), timeout=2, verbose=0)
    if ans == None:
        return False
    else:
        ans.show()
        return True

if __name__ == "__main__":
    ip_range = "10.0.0.1/24"
    arp_scan(ip_range)