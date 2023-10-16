class BankDatabase:
    def __init__(self):
        self.accounts = {
            '1234567890': {'pin': '1234', 'balance': 1000},
            '9876543210': {'pin': '4321', 'balance': 500},
            # ... more account details ...
        }

    def authenticate_card(self, card_number, pin):
        if card_number in self.accounts and self.accounts[card_number]['pin'] == pin:
            return True
        return False

    def get_balance(self, card_number):
        return self.accounts[card_number]['balance']

    def update_balance(self, card_number, amount):
        self.accounts[card_number]['balance'] += amount


class CardReader:
    def read_card(self):
        card_number = input("Please insert your card: ")
        return card_number


class Screen:
    def display_message(self, message):
        print(message)

    def display_menu(self, options):
        for option in options:
            print(option)


class Keypad:
    def get_input(self, prompt):
        return input(prompt)


class CashDispenser:
    def dispense_cash(self, amount):
        print(f"Dispensing ${amount}")


class UserSession:
    def __init__(self, account):
        self.account = account


class TransactionResult:
    SUCCESS = "Success"
    FAILURE = "Failure"


class WithdrawalTransaction:
    def __init__(self, account, amount, bank_database, cash_dispenser):
        self.account = account
        self.amount = amount
        self.bank_database = bank_database
        self.cash_dispenser = cash_dispenser

    def execute(self):
        if self.bank_database.get_balance(self.account) >= self.amount:
            self.bank_database.update_balance(self.account, -self.amount)
            self.cash_dispenser.dispense_cash(self.amount)
            return TransactionResult.SUCCESS
        return TransactionResult.FAILURE


class ATM:
    def __init__(self):
        self.bank_database = BankDatabase()
        self.card_reader = CardReader()
        self.screen = Screen()
        self.keypad = Keypad()
        self.cash_dispenser = CashDispenser()
        self.user_session = None

    def start(self):
        self.screen.display_message("Welcome to XYZ Bank ATM")
        self.insert_card()

    def insert_card(self):
        self.screen.display_message("Please insert your card.")
        inserted_card = self.card_reader.read_card()

        if inserted_card:
            self.verify_pin(inserted_card)
        else:
            self.screen.display_message("Card insertion failed. Please try again.")

    def verify_pin(self, card_number):
        pin = self.keypad.get_input("Please enter your PIN: ")
        if self.bank_database.authenticate_card(card_number, pin):
            self.user_session = UserSession(card_number)
            self.show_main_menu()
        else:
            self.screen.display_message("Invalid PIN. Please try again.")

    def show_main_menu(self):
        options = [
            "1. Check Balance",
            "2. Withdraw Cash",
            "3. Exit"
        ]

        self.screen.display_menu(options)
        choice = self.keypad.get_input("Select an option: ")

        if choice == '1':
            self.check_balance()
        elif choice == '2':
            self.withdraw_cash()
        elif choice == '3':
            self.exit()
        else:
            self.screen.display_message("Invalid choice. Please try again.")
            self.show_main_menu()

    def check_balance(self):
        balance = self.bank_database.get_balance(self.user_session.account)
        self.screen.display_message(f"Your balance is: ${balance}")
        self.show_main_menu()

    def withdraw_cash(self):
        amount = int(self.keypad.get_input("Enter amount to withdraw: "))
        transaction = WithdrawalTransaction(self.user_session.account, amount, self.bank_database, self.cash_dispenser)
        result = transaction.execute()

        if result == TransactionResult.SUCCESS:
            self.screen.display_message(f"Withdrawal of ${amount} successful. Please take your cash.")
        else:
            self.screen.display_message("Withdrawal failed. Please try again.")
        self.show_main_menu()

    def exit(self):
        self.screen.display_message("Thank you for using XYZ Bank ATM.")
        self.user_session = None
        self.insert_card()


# Main program
atm = ATM()
atm.start()
