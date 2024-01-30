


def search_and_create_file():
    # Ask the user for keywords
    keywords = input("Enter keywords (separated by commas): ").lower().split(',')

    # Ask for the file name to search
    file_name = input("Enter the file name to search: ")

    # Ask for the new file name to create
    new_file_name = input("Enter the new file name to create: ")

    # Open the existing file for reading
    with open(file_name, 'r') as old_file:
        # Open a new file for writing
        with open(new_file_name, 'w') as new_file:
            # Iterate through each line in the old file
            for line in old_file:
                # Check if any keyword is present in the line
                if any(keyword.strip().lower() in line.lower() for keyword in keywords):
                    # Write the line to the new file
                    new_file.write(line)

    print(f"Lines containing the keywords are saved in {new_file_name}.")

# Call the function to run the program
search_and_create_file()

