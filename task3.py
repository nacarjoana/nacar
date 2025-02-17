class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

account = BankAccount("09706824778", "Joana", 4000)

account.deposit(2000)
account.withdraw(1500)
account.display_balance()