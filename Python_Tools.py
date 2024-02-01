import os

out = 0


# Main Menu ----------------------

def affichagemenu():
    os.system('clear')
    os.system('toilet Power PY')
    print("\033[1;32m1-User Tools\033[m \n")
    print("\033[1;32m2-Nmap\033[m \n")
    print("\033[1;32m3-SSH\033[m \n")
    print("\033[1;33m(Q)Quitter[m \n")
    
    choix = input()
    if choix == '1':
        Usertools()
    elif choix == '2':
        nmap1()
    elif choix == 'q' or choix.lower() == 'quit':
        quiter()
    elif choix == '3':
        ssh1()
    elif choix == '4':
        affichagemenu()
    else:
        print(" Mauvais Choix ")
        pause()

#Pause -------------------------


def pause():
    print("enter to continue! ")
    input()
    affichagemenu()
    
    
#Verifier User est present dans /etc/passwd --------------

def verifyuser():
    util = input("Nom user : ")
    if not util:
        print("Veuillez entrer un nom d'utilisateur valide")
        return
    try:
        with open('/etc/passwd', 'r') as f:
            for line in f:
                if line.startswith(util + ':'):
                    print("L'utilisateur {} existe!".format(util))
                    pause()
                    return

    except FileNotFoundError:
        pass
    print("L'utilisateur est introvable\n")
    pause()


# Print UID of User X--------------------

def afficheruid():
    util = input("Nom de lutilisateur : ")
    os.system('clear')
    uid = os.popen('id {}'.format(util)).read().split()[0]
    print("L'uid de {} est : {}".format(util, uid))
    pause()


# Fin de progamme ----------------------

def quiter():
    print(" Bye Bye! ")
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
        print("maivais choix")
        pause()

# Menu SSH --------------------------

def ssh1():
    os.system('clear')
    print(" 1-SSH install\n")
    print(" 2-SSH On\n")
    print("\033[1;33m3-Main menu\033[m\n ")
    ssh1choix = input()
    if ssh1choix == '1':
        os.system('apt update && apt install openssh')
        pause()
    elif ssh1choix == '2':
        print("choix 2")
        pause()
    elif ssh1choix == '3':
        print("choix 3")
        affichagemenu()
    else:
        pass
    
    
# Menu Nmap ------------------------

def nmap1():
    os.system('clear')
    print("1-Nmap install\n")
    print("2-Nmap port ouvert\n")
    print("\033[1;33m3-Main menu\033[m\n")
    netstatchoix = input()
    if netstatchoix == '1':
        os.system('apt install nmap')
        pause()
    elif netstatchoix == '2':
        target = input("target ip (default 192.168.1.1/24): ")
        if not target:
            target = '192.168.1.1/24'
        os.system('nmap {}'.format(target))
    elif netstatchoix == '3':
        affichagemenu()
    else:
        print("Maivais choix")
        pause()
        
        
# Main function --------------------

def main1():
    while out == 0:
        os.system('clear')
        affichagemenu()
        choix = input()
        
        if choix == '1':
            Usertools()
        elif choix == '2':
            nmap1()
        elif choix == '3':
            ssh1()
        elif choix == '4':
            nmap1()
        elif choix.lower() == 'q' or choix.lower() == 'quit':
            quiter()
                        
        else:
            print(" Mauvais Choix ")
            pause()
main1()
affichagemenu()