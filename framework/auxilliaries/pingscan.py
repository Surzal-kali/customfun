from scapy.all import ICMP, IP, sr, sr1, ARP, Ether, conf

# This line disables the "MAC address not found" warnings globally
conf.verb = 0 

def arp_scan(ip_range):
    """
    Perform an ARP scan. This populates the system's ARP cache.
    """
    print(f"[*] Populating ARP cache for range: {ip_range}")
    
    # Use Ether/ARP for Layer 2 scanning
    # we wrap this in a try/except because invalid IP ranges will crash Scapy
    try:
        packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range)
        ans, unans = sr(packet, timeout=2, verbose=0)
        
        discovered = []
        for snd, rcv in ans:
            # Only add to list if the response actually contains an ARP layer
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
    # ICMP is Layer 3. Scapy will now use the ARP cache populated by arp_scan()
    ans = sr1(IP(dst=target_ip)/ICMP(), timeout=1, verbose=0)
    return ans is not None

if __name__ == "__main__":
    # Use a common range for testing, e.g., "192.168.1.0/24" or "10.0.0.0/24"
    # Note: 10.0.0.7/24 is technically a valid range, but usually 
    # network ranges end in .0/24 (e.g., 10.0.0.0/24)
    ip_range = "10.0.0.0/24" 
    
    alive_ips = arp_scan(ip_range)
    
    if not alive_ips:
        print("[-] No hosts discovered via ARP.")
    else:
        print(f"[*] {len(alive_ips)} hosts found. Verifying with ICMP...")
        for ip in alive_ips:
            if ping_scan(ip):
                print(f"  [+] {ip} is up....PONG!")
            else:
                print(f"  [-] {ip} is down (No ICMP response).")
