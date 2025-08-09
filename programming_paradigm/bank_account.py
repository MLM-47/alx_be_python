class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
            else:
                raise ValueError("Insufficient funds for withdrawal")
        else:
            raise ValueError("Withdrawal amount must be positive")

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")