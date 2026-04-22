def read_file():
    # Take filename input from the user
    file_name = input("Enter the filename to open: ")

    try:
        # Try to open the file in read mode
        with open(file_name, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)

    except FileNotFoundError:
        # Handle case where the file does not exist
        print(f"Error: The file '{file_name}' was not found.")

    except PermissionError:
        # Handle case where there are no permission to read the file
        print(f"Error: You do not have permission to read the file '{file_name}'.")

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_file()
