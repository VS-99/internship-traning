# Base class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount({self.owner}, Balance: ₹{self.balance})"

# Subclass with interest
class InterestAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # 5% by default

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied. New balance: ₹{self.balance:.2f}")

    def __str__(self):
        return f"InterestAccount({self.owner}, Balance: ₹{self.balance}, Interest Rate: {self.interest_rate * 100}%)"


# Create a standard account
account1 = BankAccount("Vallabh", 1000)
print(account1)
account1.deposit(500)
account1.withdraw(200)
print("Final Balance:", account1.get_balance())
print()

# Create an interest-bearing account
account2 = InterestAccount("Sathe", 2000, 0.1)  # 10% interest
print(account2)
account2.apply_interest()
account2.withdraw(500)
print("Final Balance with interest:", account2.get_balance())
