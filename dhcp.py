import subprocess

def configure_dhcp():
    subprocess.run(["sudo", "dhclient"])

def configure_static():
    # Gather information for static configuration
    ip_address = input("Enter IP address: ")
    netmask = input("Enter netmask: ")
    gateway = input("Enter gateway: ")

    # Create the configuration string
    config = f"""auto eth0
iface eth0 inet static
    address {ip_address}
    netmask {netmask}
    gateway {gateway}
"""

    # Write the configuration to /etc/network/interfaces
    with open("/etc/network/interfaces", "w") as file:
        file.write(config)

    # Restart networking to apply changes
    subprocess.run(["sudo", "systemctl", "restart", "networking"])

def main():
    # Ask the user whether to use DHCP or set a static configuration
    choice = input("Do you want to use DHCP? (y/n): ").lower()

    if choice == "y":
        configure_dhcp()
    elif choice == "n":
        configure_static()
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()






