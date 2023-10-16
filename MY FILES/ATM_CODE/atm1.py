class BankDatabase:
    def __init__(self):
        self.accounts = {"123456789": {"pin": "1234", "balance": 1000},
                         "987654321": {"pin": "4321", "balance": 500}}

    def authenticate_card(self, card_number, pin):
        if card_number in self.accounts and self.accounts[card_number]["pin"] == pin:
            return True
        return False

    def get_balance(self, card_number):
        return self.accounts[card_number]["balance"]

    def update_balance(self, card_number, amount):
        self.accounts[card_number]["balance"] += amount


class ATM:
    def __init__(self):
        self.bank_database = BankDatabase()
        self.user_session = None

    def start(self):
        print("Welcome to XYZ Bank ATM")
        self.insert_card()

    def insert_card(self):
        print("Please insert your card.")
        card_number = input("Card Number: ")
        pin = input("PIN: ")

        if self.bank_database.authenticate_card(card_number, pin):
            self.user_session = {"card_number": card_number}
            self.show_main_menu()
        else:
            print("Invalid card number or PIN. Please try again.")
            self.insert_card()

    def show_main_menu(self):
        print("Main Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Funds")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            self.check_balance()
        elif choice == "2":
            self.withdraw_cash()
        elif choice == "3":
            self.deposit_funds()
        elif choice == "4":
            self.exit()
        else:
            print("Invalid choice. Please try again.")
            self.show_main_menu()

    def check_balance(self):
        balance = self.bank_database.get_balance(self.user_session["card_number"])
        print(f"Your balance is: ${balance}")
        self.show_main_menu()

    def withdraw_cash(self):
        amount = int(input("Enter amount to withdraw: "))
        current_balance = self.bank_database.get_balance(self.user_session["card_number"])

        if amount <= current_balance:
            self.bank_database.update_balance(self.user_session["card_number"], -amount)
            print(f"Withdrawal successful. Please take your cash: ${amount}")
        else:
            print("Insufficient funds. Withdrawal failed.")

        self.show_main_menu()

    def deposit_funds(self):
        amount = int(input("Enter amount to deposit: "))
        self.bank_database.update_balance(self.user_session["card_number"], amount)
        print(f"Deposit successful. Thank you.")
        self.show_main_menu()

    def exit(self):
        print("Thank you for using XYZ Bank ATM.")
        self.user_session = None
        self.insert_card()


# Main Program
atm = ATM()
atm.start()
