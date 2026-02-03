class Account:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def add_money(self, amt):
        if amt > 0:
            self.balance += amt
            print(f"Amount Deposited: {amt:.2f}")
            print(f"Available Balance: {self.balance:.2f}")
        else:
            print("Enter a valid deposit amount.")

    def withdraw_money(self, amt):
        if amt > 0 and amt <= self.balance:
            self.balance -= amt
            print(f"Amount Withdrawn: {amt:.2f}")
            print(f"Available Balance: {self.balance:.2f}")
        elif amt > self.balance:
            print("Not enough balance.")
        else:
            print("Enter a valid withdrawal amount.")

    def show_balance(self):
        print(f"Balance: {self.balance:.2f}")
        return self.balance


if __name__ == "__main__":
    user_account = Account("987654321", 1500)

    while True:
        print("\n1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        option = input("Select option: ")

        if option == "1":
            user_account.show_balance()
        elif option == "2":
            value = float(input("Enter deposit amount: "))
            user_account.add_money(value)
        elif option == "3":
            value = float(input("Enter withdrawal amount: "))
            user_account.withdraw_money(value)
        elif option == "4":
            print("Thank you for banking with us.")
            break
        else:
            print("Invalid option.")
