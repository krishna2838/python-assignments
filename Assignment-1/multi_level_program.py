class Human:
    def __init__(self, person_name, person_age):
        self.person_name = person_name
        self.person_age = person_age

    def show_info(self):
        print(f"Name: {self.person_name}")
        print(f"Age: {self.person_age}")


class Staff(Human):
    def __init__(self, person_name, person_age, emp_code, pay):
        super().__init__(person_name, person_age)
        self.emp_code = emp_code
        self.pay = pay

    def show_staff_info(self):
        self.show_info()
        print(f"Employee Code: {self.emp_code}")
        print(f"Salary: {self.pay:.2f}")


class Supervisor(Staff):
    def __init__(self, person_name, person_age, emp_code, pay, dept):
        super().__init__(person_name, person_age, emp_code, pay)
        self.dept = dept

    def show_supervisor_info(self):
        self.show_staff_info()
        print(f"Department: {self.dept}")


if __name__ == "__main__":
    while True:
        print("\n1. New Person")
        print("2. New Employee")
        print("3. New Manager")
        print("4. Exit")

        select = input("Choose option: ")

        if select == "1":
            n = input("Enter name: ")
            a = int(input("Enter age: "))
            obj = Human(n, a)
            print("\nDetails:")
            obj.show_info()

        elif select == "2":
            n = input("Enter name: ")
            a = int(input("Enter age: "))
            code = input("Enter employee code: ")
            sal = float(input("Enter salary: "))
            obj = Staff(n, a, code, sal)
            print("\nDetails:")
            obj.show_staff_info()

        elif select == "3":
            n = input("Enter name: ")
            a = int(input("Enter age: "))
            code = input("Enter employee code: ")
            sal = float(input("Enter salary: "))
            dep = input("Enter department: ")
            obj = Supervisor(n, a, code, sal, dep)
            print("\nDetails:")
            obj.show_supervisor_info()

        elif select == "4":
            print("Program ended.")
            break

        else:
            print("Invalid selection.")
