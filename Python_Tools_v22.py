"""
Power PY - Python Tools
This script provides various system tools such as user management, network information, SSH functionalities, and a simple HTTP server.
For Linux systems, it includes functionalities like verifying user existence, getting user UID, scanning networks with Nmap, managing SSH connections, and running a simple HTTP server.
"""

import os
import readline
import glob
import subprocess
import time
import socket
import uuid
import psutil
import requests
import shutil


out = 0
# ---------------Pause ----------------
def pause():
    input("Press Enter to continue!")
    affichagemenu()



#Quitter ----------------------------
def quitter():
    print("Goodbye!")
    global out
    out = 1


# Main menu ---------------------------
def affichagemenu():
    os.system('clear')
    print("=" * 20 + " Power PY " + "=" * 20)
    print("\033[1;32m1-User Tools\033[m")
    print("\033[1;32m2-Network Info\033[m")
    print("\033[1;32m3-SSH\033[m")
    print("\033[1;32m4-Start Web Files Share (Python)\033[m")
    print("\033[1;33m(Q)Quitter\033[m")
    print("=" * 50)
    #----------------------------------------


    
    choix = input("Enter your choice: ")
    if choix == '1':
        Usertools()
    elif choix == '2':
        NetworkInfo()
    elif choix == '3':
        ssh1()
    elif choix == '4':
            serverx()
    elif choix.lower() in ['q', 'quit']:
        quitter()
    else:
        print("Invalid Choice")
        pause()



# --------------------User Tools ------- 
def Usertools():
    os.system('clear')
    print("1-Verify user existence\n")
    print("2-Get user UID\n")
    print("\033[1;33m3-Main menu\033[m\n")
    #---------------------------------------




    Usertools_choix = input("Choose 1-3: \n")
    match Usertools_choix:
        case '1':
            verifyuser()
        case '2':
            afficheruid()
        case '3':
            affichagemenu()
        case _:
            print("Invalid choice")
            pause()

# Verify User exists in /etc/passwd ---- 
def verifyuser():
    util = input("Username: ")
    if not util:
        print("Please enter a valid username")
        pause()
        return
        
    try:
        with open('/etc/passwd', 'r') as f:
            for line in f:
                if line.startswith(util + ':'):
                    print(f"User {util} exists!")
                    pause()
                    return
        print("User not found\n")
    except FileNotFoundError:
        print("File /etc/passwd not found")
    pause()




def afficheruid():
    util = input("Username: ")
    os.system('clear')
    uid = os.popen(f'id {util}').read().split()[0]
    print(f"UID of {util} is: {uid}")
    pause()

# --------------------------------- Network Info -----------------------------

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

# Nmap ---------------------------------

def NetworkInfo():
    os.system('clear')
    print("1-Nmap install\n")
    print("2-Nmap Quick Scan\n")
    print("3-Nmap Os Info\n")
    print("4-Info network interfaces\n")
    print("\033[1;33m5-Main menu\033[m\n")
    #---------------------------------------



    NetworkInfo_choix = input("Choose 1-3: ")
    match NetworkInfo_choix:
        case '1':
            install_nmap()
                                  
        case '2':
            TargetIp_Range = input("Network Ip (192.xxx.xxx.0/24)")
            os.system(f'nmap -sP {TargetIp_Range}')
            pause()

        case '3':
            TargetIp_Range2 = input("Host Ip (192.xxx.xxx.xxx)")
            os.system(f'sudo nmap -O {TargetIp_Range2}')
            pause()

        case '4':
            os.system('clear')
            display_network_info()    
            print("Checking network interfaces")
            pause()                
    
        case '5':
            affichagemenu()

def install_nmap():
    """
    Installe nmap en supportant seulement apt (Debian/Ubuntu) et pacman (Arch).
    Utilise sudo et vérifie l'installation.
    """
    # detect package manager
    if shutil.which("pacman"):
        cmd = ["sudo", "pacman", "-S", "--noconfirm", "nmap"]
        use_shell = False
    elif shutil.which("apt"):
        # apt update && apt install -y nmap
        cmd = "sudo apt update && sudo apt install -y nmap"
        use_shell = True
    else:
        print("Ni apt ni pacman trouvés — installe nmap manuellement.")
        return

    try:
        print("Running:", cmd if use_shell else " ".join(cmd))
        if use_shell:
            subprocess.run(cmd, shell=True, check=True)
        else:
            subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("Échec de l'installation :", e)
        return

# SSH ----------------------------------
def ssh1():
    os.system('clear')
    print("1-SSH install\n")
    print("2-SSH On\n")
    print("3-File Transfer(SCP)\n")
    print("\033[1;33m4-Main menu\033[m\n")
#---------------------------------------  




    ssh1choix = input("Choose 1-4: ")
    match ssh1choix:
        case '1':
            os.system('apt update && apt install openssh')
            pause()
        case '2':
            print("Option 2")
            os.system('systemctl start ssh')
            pause()
        case '3':
            print("1-Upload file\n")
            print("2-Download file\n")
            print("3-Main menu\n")
            ssh1choix = input("Choose 1-3ipa: ")
            if ssh1choix == '1':
                print("Upload file")
                # Enable path completion for this input
                readline.set_completer(complete_path)
                path = input("Enter the path of the file to upload (use TAB to autocomplete): ")
                readline.set_completer(None)  # Disable completion for other inputs
                User = input("Enter the username: ")
                Ip_address = input("Enter the IP address: ")
                path_remote = input("Enter the path to upload the file: ")
                os.system(f'scp {path} {User}@{Ip_address}:{path_remote}')
                pause()
            elif ssh1choix == '2':
                print("Download file")
                User = input("Enter the username: ")
                Ip_address = input("Enter the IP address: ")
                path_remote = input("Enter the path to download the file: ")
                os.system(f'scp {User}@{Ip_address}:{path_remote} .')
                pause()
            elif ssh1choix == '3':
                affichagemenu()
        case '4':
            affichagemenu()
        case _:
            print("Invalid choice")
            pause()
            
            



# Server X ----------------------------
def serverx():
    time_hold = input("Time to run ?/(Minute) ")

    try:
        # Start the server process
        server_process = subprocess.Popen(["python3", "-m", "http.server", "8080"])
        
        # Wait for the specified time
        time.sleep(float(time_hold) * 60)
        
        print(f"Time over after {time_hold} minutes!")
        server_process.terminate()  # Stop the server
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        server_process.terminate()
    except ValueError:
        print("Please enter a valid number for minutes")







# --------------------Main menu------------- 
def main1():
    while out == 0:
        affichagemenu()        
def complete_path(text, state):
    """Tab completion function for file paths"""
    if '~' in text:
        text = os.path.expanduser(text)
    
    if os.path.isdir(text):
        text += '/'
    
    dir_name = os.path.dirname(text)
    if dir_name == '':
        dir_name = '.'
    
    matches = glob.glob(os.path.join(dir_name, text + '*'))
    matches = [x + ('/' if os.path.isdir(x) else '') for x in matches]
    return matches[state] if state < len(matches) else None
# Enable tab completion
readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")

if __name__ == '__main__':
    main1()