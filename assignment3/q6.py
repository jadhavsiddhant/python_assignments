# 6. Write a Python class BankAccount with attributes like account_number,  balance, date_of_opening 
# and customer_name, and methods like deposit,  withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")

# Sample usage
account = BankAccount("1234567890", "Alice Smith", "2023-01-01", 1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(300)

# Check balance
account.check_balance()