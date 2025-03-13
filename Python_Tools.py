import os
import readline
import glob

out = 0

# Main Menu ----------------------
def affichagemenu():
    os.system('clear')
    print("=" * 20 + " Power PY " + "=" * 20)
    print("\033[1;32m1-User Tools\033[m")
    print("\033[1;32m2-Nmap\033[m")
    print("\033[1;32m3-SSH\033[m")
    print("\033[1;32m4-Run web files server\033[m")
    print("\033[1;33m(Q)Quitter\033[m")
    print("=" * 50)
    
    choix = input("Enter your choice: ")
    if choix == '1':
        Usertools()
    elif choix == '2':
        nmap1()
    elif choix == '3':
        ssh1()
    elif choix == '4':
        web_server()
    elif choix.lower() in ['q', 'quit']:
        quiter()
    else:
        print("Invalid Choice")
        pause()

def web_server():
    os.system('clear')
    print("1-Run web files server\n")
    print("2-Main menu\n")
    choix = input("Enter your choice: ")
    if choix == '1':
        print("Web files server running on port 8585")
        my_ip = os.popen('ifconfig | grep "inet " | grep -v 127.0.0.1 | awk "{print $2}"').read().strip()
        print(f"Web files server running on {my_ip}:8585")

        os.system('python3 -m http.server 8585')
        pause()

    elif choix == '2':
        affichagemenu()
    else:
        print("Invalid Choice")
        pause()

#### Pause -------------------------
def pause():
    input("Press Enter to continue!")
    affichagemenu()

#### Verify User exists in /etc/passwd --------------
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

#### Print UID of User X--------------------
def afficheruid():
    util = input("Username: ")
    os.system('clear')
    uid = os.popen(f'id {util}').read().split()[0]
    print(f"UID of {util} is: {uid}")
    pause()

#### Program Exit ----------------------
def quiter():
    print("Goodbye!")
    global out
    out = 1

# User Tools menu ---------------------
def Usertools():
    os.system('clear')
    print("1-Verify user existence\n")
    print("2-Get user UID\n")
    print("\033[1;33m3-Main menu\033[m\n")
    
    usert = input("Choose 1-3: \n")
    if usert == '1':
        verifyuser()
    elif usert == '2':
        afficheruid()
    elif usert == '3':
        affichagemenu()
    else:
        print("Invalid choice")
        pause()

# Menu SSH --------------------------
def ssh1():
    os.system('clear')
    print("1-SSH install\n")
    print("2-SSH On\n")
    print("3-File Transfer\n")
    print("\033[1;33m4-Main menu\033[m\n")
    
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
            print("Option 3")
            print("1-Upload file\n")
            print("2-Download file\n")
            print("3-Main menu\n")
            ssh1choix = input("Choose 1-5: ")
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
                pause()
            elif ssh1choix == '3':
                affichagemenu()
        case '4':
            affichagemenu()

# Menu Nmap ------------------------
def nmap1():
    os.system('clear')
    print("1-Nmap install\n")
    print("2-Scan open ports\n")
    print("3-Scan Fast\n")
    print("\033[1;33m4-Main menu\033[m\n")
    
    netstatchoix = input("Choose 1-3: ")
    match netstatchoix:
        case '1':
            os.system('apt install nmap')
            pause()
        case '2':
            target = input("Target IP (default 192.168.2.0/24): ") or '192.168.2.0/24'
            os.system(f'nmap {target} > scan_open_ports.txt')
            print("Scan saved to scan_open_ports.txt")
            pause() 
        case '3':
            target = input("Target IP (default 192.168.2.0/24): ") or '192.168.2.0/24'
            os.system(f'nmap -F {target} > scan_fast.txt')
            print("Scan saved to scan_fast.txt")
            pause()
        case '4':
            affichagemenu()
        case _:
            print("Invalid choice")
            pause()

# Main function --------------------
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
