# pip install scapy openpyxl netifaces


import os
import socket
import netifaces
from scapy.all import ARP, Ether, srp
import tkinter as tk
from openpyxl import Workbook
import ipaddress
import concurrent.futures

OUTPUT_FILE = "network_scan.xlsx"
TIMEOUT = 1  # Timeout in seconds for ARP requests

def get_interfaces():
    """Return a list of available interfaces with IPv4 info."""
    interfaces = []
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            ipv4_info = addrs[netifaces.AF_INET][0]
            ip = ipv4_info.get('addr')
            netmask = ipv4_info.get('netmask')
            if ip and netmask and not ip.startswith("127."):  # skip loopback
                interfaces.append({
                    "name": iface,
                    "ip": ip,
                    "mask": netmask
                })
    return interfaces

def choose_interface(interfaces):
    """Ask the user which interface to use."""
    print("\nAvailable network interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i}: {iface['name']}  IP={iface['ip']}  MASK={iface['mask']}")
    while True:
        try:
            choice = int(input("Select interface number to scan: "))
            if 0 <= choice < len(interfaces):
                return interfaces[choice]
        except ValueError:
            pass
        print("Invalid choice. Try again.")

def subnet_from_ip(ip, mask):
    """Convert IP and netmask to CIDR subnet (e.g. 192.168.1.0/24)."""
    network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
    return str(network)

def send_arp_request(target_ip):
    """Send an ARP request to a single target IP."""
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    response = srp(packet, timeout=TIMEOUT, verbose=0)[0]
    
    devices = []
    for sent, received in response:
        ip = received.psrc
        mac = received.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        devices.append({"ip": ip, "mac": mac, "name": hostname})
    return devices

def scan_network_parallel(target_subnet):
    """Scan network using multithreading for faster ARP requests."""
    devices = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:  # Limiting to 10 threads
        # Generate a list of IPs in the target subnet
        ips = [str(ip) for ip in ipaddress.IPv4Network(target_subnet).hosts()]
        
        # Asynchronously send ARP requests to all IPs
        futures = {executor.submit(send_arp_request, ip): ip for ip in ips}
        
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                devices.extend(result)
            except Exception as e:
                print(f"[!] Error scanning {futures[future]}: {e}")
    return devices

def save_to_excel(devices, filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "Network Scan"
    ws.append(["IP Address", "MAC Address", "Device Name"])
    for d in devices:
        ws.append([d['ip'], d['mac'], d['name']])
    wb.save(filename)

if __name__ == "__main__":
    # Step 1: Get interfaces
    interfaces = get_interfaces()
    if not interfaces:
        print("No active network interfaces detected.")
        exit(1)

    # Step 2: User selects one
    selected_iface = choose_interface(interfaces)
    subnet = subnet_from_ip(selected_iface['ip'], selected_iface['mask'])
    print(f"[*] Scanning subnet {subnet} on interface {selected_iface['name']}...")

    # Step 3: Scan in parallel
    devices = scan_network_parallel(subnet)
    if not devices:
        print("[!] No devices found on this subnet.")
    else:
        print(f"[+] Found {len(devices)} devices.")
        for d in devices:
            print(f"{d['ip']:15} {d['mac']:17} {d['name']}")
        save_to_excel(devices, OUTPUT_FILE)
        print(f"[+] Results saved to {OUTPUT_FILE}")
