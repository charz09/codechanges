class Account:
    def __init__(self, account_number, pin, balance, account_type):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.account_type = account_type

class BankDatabase:
    def __init__(self):
        self.accounts = {
            "123456789": Account("123456789", "1234", 1000, "Savings"),
            "987654321": Account("987654321", "4321", 500, "Checking")
        }

    def authenticate_card(self, card_number, pin):
        if card_number in self.accounts and self.accounts[card_number].pin == pin:
            return True
        return False

    def get_account(self, card_number):
        return self.accounts[card_number]

    def update_balance(self, account, amount):
        self.accounts[account.account_number].balance += amount


class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.75}

    def convert_to_usd(self, amount, currency):
        return amount / self.exchange_rates[currency]


class ATM:
    def __init__(self):
        self.bank_database = BankDatabase()
        self.currency_converter = CurrencyConverter()
        self.user_session = None

    def start(self):
        print("Welcome to XYZ Bank ATM")
        self.insert_card()

    def insert_card(self):
        print("Please insert your card.")
        card_number = input("Card Number: ")
        pin = input("PIN: ")

        if self.bank_database.authenticate_card(card_number, pin):
            self.user_session = self.bank_database.get_account(card_number)
            self.show_main_menu()
        else:
            print("Invalid card number or PIN. Please try again.")
            self.insert_card()

    def show_main_menu(self):
        print(f"Main Menu - {self.user_session.account_type} Account")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Funds")
        print("4. Currency Conversion")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            self.check_balance()
        elif choice == "2":
            self.withdraw_cash()
        elif choice == "3":
            self.deposit_funds()
        elif choice == "4":
            self.currency_conversion()
        elif choice == "5":
            self.exit()
        else:
            print("Invalid choice. Please try again.")
            self.show_main_menu()

    def check_balance(self):
        print(f"Your balance is: ${self.user_session.balance}")
        self.show_main_menu()

    def withdraw_cash(self):
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= self.user_session.balance:
            self.bank_database.update_balance(self.user_session, -amount)
            print(f"Withdrawal successful. Please take your cash: ${amount}")
        else:
            print("Insufficient funds. Withdrawal failed.")

        self.show_main_menu()

    def deposit_funds(self):
        amount = float(input("Enter amount to deposit: $"))
        self.bank_database.update_balance(self.user_session, amount)
        print(f"Deposit successful. Thank you.")
        self.show_main_menu()

    def currency_conversion(self):
        print("Currency Conversion:")
        amount = float(input("Enter amount: $"))
        currency = input("Enter currency (USD, EUR, GBP): ").upper()

        if currency in self.currency_converter.exchange_rates:
            usd_equivalent = self.currency_converter.convert_to_usd(amount, currency)
            print(f"Equivalent in USD: ${usd_equivalent:.2f}")
        else:
            print("Invalid currency.")

        self.show_main_menu()

    def exit(self):
        print("Thank you for using XYZ Bank ATM.")
        self.user_session = None
        self.insert_card()


# Main Program
atm = ATM()
atm.start()
