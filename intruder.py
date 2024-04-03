from scapy.all import ARP, Ether, srp
import time

def scan_network(network):
    """
    Scans the network using ARP requests and returns a set of IP addresses.
    """
    arp_request = ARP(pdst=network)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return {sent.psrc for sent, received in answered_list}

def main():
    known_ips = set()
    network = "192.168.2.0/24"  # Adjust this to your network

    while True:
        current_ips = scan_network(network)
        new_ips = current_ips - known_ips
        if new_ips:
            print("New IP(s) detected:", new_ips)
            known_ips.update(new_ips)
        else:
            print("No new IPs detected.")

        time.sleep(60)  # Scan every 60 seconds

if __name__ == "__main__":
    main()

