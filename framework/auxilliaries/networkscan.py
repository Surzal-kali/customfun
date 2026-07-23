from scapy.all import ICMP, IP, sr, sr1, ARP, Ether, conf, TCP
import socket
from ipaddress import ip_network
import logging

# Disable the default scapy verbosity
# This line disables the "MAC address not found" warnings globally
conf.verb = 0 

# Set the logging level to ERROR to suppress warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def sendp_custom(packet, *args, **kwargs):
    try:
        return sr1(packet, *args, **kwargs)
    except Exception as e:
        print(f"[-] Error during packet send: {e}")
        return None, None

def syn_scan(ip_range, port=443):
    print(f"[*] Performing batch SYN scan on {port}...")
    # Create a list of packets
    packets = [IP(dst=str(ip))/TCP(dport=port, flags="S") for ip in ip_range]
    ans, unans = sendp_custom(packets, timeout=2, verbose=0) 
    
    if ans:
        for snd, rcv in ans:
            if rcv.haslayer(TCP) and rcv[TCP].flags == 0x12: # SYN-ACK
                print(f"[*] {rcv.src} is open on port {port}")
            elif rcv.haslayer(TCP) and rcv[TCP].flags == 0x14: # RST
                print(f"[-] {rcv.src} is up but port {port} is closed")
    else:
        print("No hosts responded to SYN scan")

def arp_scan(ip_range):
    """
    Perform an ARP scan. This populates the system's ARP cache.
    """
    print(f"[*] Populating ARP cache for range: {ip_range}")
    
    try:
        # If ip_range is a list of IPv4Address objects, 
        # Scapy will crash. We check if it's a list and convert to strings,
        # or if it's already a CIDR string, we leave it.
        if isinstance(ip_range, list):
            # Scapy can handle a list of strings for pdst
            target_range = [str(ip) for ip in ip_range]
        else:
            target_range = ip_range

        packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_range)
        ans, unans = sendp_custom(packet, timeout=10, verbose=0)
        
        discovered = []
        for snd, rcv in ans:
            if rcv.haslayer(ARP):
                discovered.append(rcv[ARP].psrc)
                print(f"Found: {rcv[ARP].psrc} -> {rcv[Ether].src}")
        
        return discovered
    except Exception as e:
        print(f"[-] Error during ARP scan: {e}")
        return []

def ping_scan(target_ip):
    """
    Perform a ping scan on a specific target.
    """
    # Convert IPv4Address object to string
    target_ip = str(target_ip)
    
    # ICMP is Layer 3. Scapy will now use the ARP cache populated by arp_scan()
    ans = sr1(IP(dst=target_ip)/ICMP(), timeout=10, verbose=0)
    return ans is not None

if __name__ == "__main__":
    # Keep the string version for the ARP scan because it's faster/native
    cidr_range = "10.0.0.0/24"
    # Keep the list version for the SYN scan because we iterate/process them
    ip_list = list(ip_network(cidr_range, strict=False))

    # 1. ARP Scan first (Use the CIDR string)
    discovered_ips = arp_scan(cidr_range)

    # 2. SYN Scan second (Use the list)
    syn_scan(ip_list)

    # Test ping scan on the first discovered IP
    if discovered_ips:
        target_ip = discovered_ips[0]
        if ping_scan(target_ip):
            print(f"{target_ip} is up.")
        else:
            print(f"{target_ip} is down.")
    else:
        print("No hosts found.")
