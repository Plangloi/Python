import subprocess
import os


def clear_screen():
    """Clears the screen for a cleaner presentation."""
    if os.name == 'posix':  # For Linux/macOS
        os.system('clear')
    else:
        os.system('cls')  # For Windows


def menu():
    """Displays the main menu."""
  #  clear_screen()
    print("\n--- Main Menu ---")
    print("1. System info")
    print("2. Network Tools")
    print("3. Admin Tools")  # Placeholder for future functionality
    print("4. File Share")   # Placeholder for future functionality
    print("5. Exit")


def menu_system():
    """Presents options for displaying system information."""
  #  clear_screen()
    print("1. Display OS Information")
    print("2. Display Users with UID")
    print("3. Show Network Connections")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # Add logic to handle user choices
    # For example:
    if choice == '1':
        # Display OS information cat /etc/os-release
        os_info = subprocess.check_output(['cat', '/etc/os-release']).decode('utf-8')
        print(os_info)

    elif choice == '2':
         # Display users with UID
         user_info = subprocess.check_output(['cut', '-d:', '-f1,3', '/etc/passwd']).decode('utf-8')
         print(user_info)

    elif choice == '3':
         # Show network connections 
         network_info = subprocess.check_output(['netstat', '-tuln']).decode('utf-8')
         print(network_info)
         
    elif choice == '4':
    #     # Exit the program
        return
        
    else:
        print("Invalid choice. Please try again.")


def main():
    """Main loop for the program."""
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            menu_system()
        elif choice == '2':
            # Add functionality for network tools here
            print("Network tools section under development.")
        elif choice == '3':
            # Add functionality for admin tools here
            print("Admin tools section under development.")
        elif choice == '4':
            # Add functionality for file share here
            print("File share section under development.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-5).")


if __name__ == "__main__":
    main()

