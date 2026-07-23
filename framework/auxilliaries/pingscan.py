from scapy.all import ICMP, IP, sr, sr1, ARP, Ether

def arp_scan(ip_range):
    """
    Perform an ARP scan on the given IP range.
    """
    # Use sr() instead of sr1() to scan a range and get multiple responses
    ans, unans = sr(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=2, verbose=0)
    for snd, rcv in ans:
        if rcv is not None:
            # Fixed the nested quotes in the f-string
            print(f"IP: {rcv[ARP].psrc} MAC: {rcv[Ether].src}")

def ping_scan(ip_range):
    """
    Perform a ping scan on the given IP range.
    """
    # For a single target, sr1 is fine. 
    # For a range, you should iterate through IPs or use sr()
    ans = sr1(IP(dst=ip_range)/ICMP(), timeout=2, verbose=0)
    if ans is None:
        return False
    else:
        ans.show()
        return True

if __name__ == "__main__":
    # Note: Ensure you run this as sudo/Administrator for raw socket access
    ip_range = "10.0.0.1/24"
    arp_scan(ip_range)
    ping_scan(ip_range)
    for ip in ip_range.split("/")[0]:
        print(ip)