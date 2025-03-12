import os
from tkinter import *
import ttkbootstrap as tb

# Create the main window
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')  # Fixed geometry string format
root.mainloop()

out = 0

# Main Menu ----------------------
def affichagemenu():
    os.system('clear')
    os.system('toilet Power PY')
    print("\033[1;32m1-User Tools\033[m \n")
    print("\033[1;32m2-Nmap\033[m \n") 
    print("\033[1;32m3-SSH\033[m \n")
    print("\033[1;33m(Q)Quitter\033[m \n")
    
    choix = input()
    if choix == '1':
        Usertools()
    elif choix == '2':
        nmap1()
    elif choix == '3':
        
        ssh1()
    elif choix.lower() in ['q', 'quit']:
        quiter()
    else:
        print("Mauvais Choix")
        pause()

# Pause -------------------------
def pause():
    input("Enter to continue!")
    affichagemenu()

# Verify User exists in /etc/passwd --------------
def verifyuser():
    util = input("Nom user : ")
    if not util:
        print("Veuillez entrer un nom d'utilisateur valide")
        pause()
        return
        
    try:
        with open('/etc/passwd', 'r') as f:
            for line in f:
                if line.startswith(util + ':'):
                    print(f"L'utilisateur {util} existe!")
                    pause()
                    return
        print("L'utilisateur est introuvable\n")
    except FileNotFoundError:
        print("Fichier /etc/passwd non trouvé")
    pause()

# Print UID of User X--------------------
def afficheruid():
    util = input("Nom de l'utilisateur : ")
    os.system('clear')
    uid = os.popen(f'id {util}').read().split()[0]
    print(f"L'uid de {util} est : {uid}")
    pause()

# Program Exit ----------------------
def quiter():
    print("Bye Bye!")
    global out
    out = 1

# User Tools menu ---------------------
def Usertools():
    os.system('clear')
    print("1-Vérifier l'existence d'un utilisateur\n")
    print("2-Connaître l'UID d'un utilisateur\n")
    print("\033[1;33m3-Main menu\033[m\n")
    
    usert = input("Choisir 1-3 : \n")
    if usert == '1':
        verifyuser()
    elif usert == '2':
        afficheruid()
    elif usert == '3':
        affichagemenu()
    else:
        print("Mauvais choix")
        pause()

#
def ssh1():
    os.system('clear')
    print("1-SSH install\n")
    print("2-SSH On\n")
    print("\033[1;33m3-Main menu\033[m\n")
    
    ssh1choix = input()
    if ssh1choix == '1':
        os.system('apt update && apt install openssh')
        pause()
    elif ssh1choix == '2':
        print("choix 2")
        pause()
    elif ssh1choix == '3':
        affichagemenu()

# Menu Nmap ------------------------
def nmap1():
    os.system('clear')
    print("1-Nmap install\n")
    print("2-Nmap port ouvert\n")
    print("3-Nmap scan for Os\n")
    print("4-Nmap scan all ports\n")
    print("\033[1;33m3-Main menu\033[m\n")
    
    # 
    netstatchoix = input()
    match netstatchoix:
        case '1':
            os.system('apt install nmap')
            pause()
        case '2':
            target = input("target ip (default 192.168.1.1/24): ") or '192.168.1.1/24'
            os.system(f'nmap {target}')
            pause()
        case '3':
            print("choix 3")
            target = input("target ip (default 192.168.1.1/24): ") or '192.168.1.1/24'
            os.system(f'nmap -O {target}')
            pause()

        case '4':
            target = input("target ip (default 192.168.1.1/24): ") or '192.168.1.1/24'
            os.system(f'nmap -p- {target}')
            pause()
        case _:
            print("Mauvais choix")
            pause()
# Main function --------------------
def main1():
    while out == 0:
        affichagemenu()
        
if __name__ == '__main__':
    main1()
