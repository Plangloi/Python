from scapy.all import ARP, Ether, srp

def check_mac_address(mac_address, network_interface='en0'):
    # Create an ARP request packet to check for the MAC address
    arp_request = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst='192.168.1.0/24')

    # Send the ARP request packet and capture the response
    result = srp(arp_request, timeout=3, iface=network_interface, verbose=False)[0]

    # Check the response for the desired MAC address
    for sent, received in result:
        if received[ARP].hwsrc == mac_address:
            return True

    return False
# Usage
network_interface = input("Enter the network interface name: ")
target_mac = network_interface
is_present = check_mac_address(target_mac)

if is_present:
    print(f"The MAC address {target_mac} is present on the network.")
else:
    print(f"The MAC address {target_mac} is not present on the network.")
