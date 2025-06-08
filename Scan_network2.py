import socket
import uuid
import psutil
import requests

def get_hostname():
    return socket.gethostname()

def get_local_ip():
    try:
        return socket.gethostbyname(get_hostname()) #
    except socket.gaierror:
        return "Unable to get Local IP"

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=text', timeout=5)
        return response.text
    except requests.RequestException:
        return "Unable to fetch Public IP"

def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

def get_network_interfaces():
    interfaces = {}
    for interface_name, interface_addresses in psutil.net_if_addrs().items():
        interfaces[interface_name] = []
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                interfaces[interface_name].append(address.address)
    return interfaces

def display_network_info():
    print("Hostname       :", get_hostname())
    print("Local IP       :", get_local_ip())
    print("Public IP      :", get_public_ip())
    print("MAC Address    :", get_mac_address())
    print("\nNetwork Interfaces and IPs:")
    interfaces = get_network_interfaces()
    for name, ips in interfaces.items():
        print(f" - {name}: {', '.join(ips)}")

if __name__ == "__main__":
    display_network_info()
