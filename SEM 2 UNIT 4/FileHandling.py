# Program demonstrating fundamental file handling operations

def file_operations():
    # 1. Opening a file and writing to it
    with open("example.txt", "w") as file:
        file.write("This is the first line of the file.\n")
        file.write("This is the second line of the file.\n")
    print("File written successfully.")

    # 2. Opening the file and reading its contents
    with open("example.txt", "r") as file:
        contents = file.read()
        print("\nContents of the file:")
        print(contents)

    # 3. Appending additional content to the file
    with open("example.txt", "a") as file:
        file.write("This is the appended line.\n")
    print("\nContent appended successfully.")

    # 4. Re-reading the file to show the appended content
    with open("example.txt", "r") as file:
        updated_contents = file.read()
        print("\nUpdated contents of the file after appending:")
        print(updated_contents)

if __name__ == "__main__":
    file_operations()
