def search_and_calculate_sum():
    # Ask the user for keywords
    keywords = input("Enter keywords (separated by commas): ").lower().split(',')

    # Ask for the file name to search
    file_name = input("Enter the file name to search: ")

    # Ask for the new file name to create
    new_file_name = input("Enter the new file name to create: ")

    # Open the existing file for reading with error handling for encoding
    try:
        with open(file_name, 'r', encoding='utf-8') as old_file:
            # Open a new file for writing
            with open(new_file_name, 'w') as new_file:
                # Initialize a variable to store the sum of the 7th column
                column_7_sum = 0

                # Iterate through each line in the old file
                for line in old_file:
                    # Check if any keyword is present in the line (case-insensitive)
                    if any(keyword.strip().lower() in line.lower() for keyword in keywords):
                        # Write the line to the new file
                        new_file.write(line)

                        # Split the line into columns using space as the delimiter
                        columns = line.split()

                        # Try to convert the 7th column to a float and add it to the sum
                        try:
                            column_7_sum += round(float(columns[2]),2)
                        except (ValueError, IndexError):
                            print("Warning: Unable to extract or convert the 7th column to a number.")

                print(f"Lines containing the keywords are saved in {new_file_name}.")
                print(f"Sum of the 3rd column: {round(column_7_sum, 2)}")

    except UnicodeDecodeError:
        print("Error: Unable to decode the file with 'utf-8' encoding. Trying 'latin-1' encoding.")

        # Retry opening the file with 'latin-1' encoding
        with open(file_name, 'r', encoding='latin-1') as old_file:
            # Open a new file for writing
            with open(new_file_name, 'w') as new_file:
                # Initialize a variable to store the sum of the 7th column
                column_7_sum = 0

                # Iterate through each line in the old file
                for line in old_file:
                    # Check if any keyword is present in the line (case-insensitive)
                    if any(keyword.strip().lower() in line.lower() for keyword in keywords):
                        # Write the line to the new file
                        new_file.write(line)

                        # Split the line into columns using space as the delimiter
                        columns = line.split()

                        # Try to convert the 7th column to a float and add it to the sum
                        try:
                            column_7_sum += round(float(columns[2]),2)
                        except (ValueError, IndexError):
                            print("Warning: Unable to extract or convert the 7th column to a number.")

                print(f"Lines containing the keywords are saved in {new_file_name}.")
                print(f"Sum of the 3rd column: {round(column_7_sum, 2)}")


# Call the function to run the program
search_and_calculate_sum()
