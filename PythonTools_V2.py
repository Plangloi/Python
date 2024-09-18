#Tools

import subprocess
import os

def menu():
    print("\n--- Main Menu ---")
    print("1. System info")
    print("2. Network Tools")
    print("3. Admin Tools")
    print("4. File Share")
    print("5. Exit")


def menu_system():
    os.system('clear')
    while True:
        print("1. Display OS Information")
        print("2. Display Users with UID >= 1000")
        print("3. Show Network Connections")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            # Run the command to display OS information
            subprocess.run(["cat", "/etc/os-release"])
        elif choice == '2':
            # Run the awk command to filter users with UID >= 1000
            subprocess.run(["awk", "-F:", "$3 >= 1000 { print $1 }", "/etc/passwd"])
        elif choice == '3':
            # Run the command to display network information
            subprocess.run(["nmcli"])
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")
        
#================================-Main-=========================================================

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            menu_system()
        elif choice == '2':
            add_numbers()
        elif choice == '3':
            subtract_numbers()
        elif choice == '4':
            multiply_numbers()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
