class Book:
    def __init__(self, title, writer, status=True):
        self.title = title
        self.writer = writer
        self.status = status

    def issue(self):
        if self.status:
            self.status = False
            print(f"{self.title} by {self.writer} has been issued.")
        else:
            print(f"{self.title} by {self.writer} is not available right now.")

    def submit(self):
        if not self.status:
            self.status = True
            print(f"{self.title} by {self.writer} has been returned.")
        else:
            print(f"{self.title} by {self.writer} was not issued.")

    def show_details(self):
        current = "Available" if self.status else "Not Available"
        print(f"{self.title} by {self.writer} - {current}")


if __name__ == "__main__":
    books_list = [
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("The Great Gatsby", "F. Scott Fitzgerald")
    ]

    while True:
        print("\n1. Show Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        user_choice = input("Enter your option: ")

        if user_choice == "1":
            for item in books_list:
                item.show_details()

        elif user_choice == "2":
            name = input("Enter book name to issue: ")
            for item in books_list:
                if item.title.lower() == name.lower():
                    item.issue()
                    break
            else:
                print("Book not found.")

        elif user_choice == "3":
            name = input("Enter book name to return: ")
            for item in books_list:
                if item.title.lower() == name.lower():
                    item.submit()
                    break
            else:
                print("Book not found.")

        elif user_choice == "4":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid option.")
