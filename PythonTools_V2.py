def menu():
    print("\n--- Main Menu ---")
    print("1. System info")
    print("2. Network Tools")
    print("3. Admin Tools")
    print("4. File Share")
    print("5. Exit")

def say_hello():
    print("Hello!")

def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The result is: {num1 + num2}")

def subtract_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The result is: {num1 - num2}")

def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The result is: {num1 * num2}")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            say_hello()
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