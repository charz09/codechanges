class BankDatabase:
    def __init__(self):
        self.accounts = {
            '1234567890': {'pin': '1234', 'balance': 1000},
            '9876543210': {'pin': '4321', 'balance': 500},
            '4326789654': {'pin': '7777', 'balance': 3000},
            # ... more account details ...
        }

    def authenticate_card(self, card_numbers, pin):
        if card_numbers in self.accounts and self.accounts[card_numbers]['pin'] == pin:
            # provide the return to be true
            return True
        return False

    def get_balance(self, card_numbers):
        return self.accounts[card_numbers]['balance']

    def update_balance(self, card_numbers, cash):
        self.accounts[card_numbers]['balance'] += cash


class CardReader:
    def read_card(self):
        card_numbers = input("Please insert your card: ")
        return card_numbers


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
    def dispense_cash(self, cash):
        print(f"Dispensing ${cash}")


class UserSession:
    def __init__(self, account):
        self.account = account


class TransactionResult:
    SUCCESS = "Success"
    FAILURE = "Failure"


class WithdrawalTransaction:
    def __init__(self, account, cash, bank_database, cash_dispenser):
        self.account = account
        self.cash = cash
        self.bank_database = bank_database
        self.cash_dispenser = cash_dispenser

    def execute(self):
        if self.bank_database.get_balance(self.account) >= self.cash:
            self.bank_database.update_balance(self.account, -self.cash)
            self.cash_dispenser.dispense_cash(self.cash)
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

    def verify_pin(self, card_numbers):
        pin = self.keypad.get_input("Please enter your PIN: ")
        if self.bank_database.authenticate_card(card_numbers, pin):
            self.user_session = UserSession(card_numbers)
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
        cash = int(self.keypad.get_input("Enter cash to withdraw: "))
        transaction = WithdrawalTransaction(self.user_session.account, cash, self.bank_database, self.cash_dispenser)
        result = transaction.execute()

        if result == TransactionResult.SUCCESS:
            self.screen.display_message(f"Withdrawal of ${cash} successful. Please take your cash.")
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
