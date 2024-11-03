# Base class for a bank account
class BankAccount:
    # Constructor method to initialize a BankAccount object
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance               # Protected attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient funds or invalid amount.")

    # Method to get the current balance
    def get_balance(self):
        return self._balance


# Derived class for a savings account with interest
class SavingsAccount(BankAccount):
    # Constructor for SavingsAccount, including an interest rate
    def __init__(self, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_holder, balance)  # Initialize parent class attributes
        self.interest_rate = interest_rate         # Additional attribute for interest rate

    # Method to add interest to the account balance
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)  # Add interest to the balance using deposit method
        print(f"Interest of {interest} added to balance.")


# Derived class for a current account with an overdraft notification
class CurrentAccount(BankAccount):
    # Overriding the withdraw method for overdraft notification
    def withdraw(self, amount):
        if amount > self._balance:
            print("Overdraft: Withdrawal exceeds current balance.")
        else:
            super().withdraw(amount)  # Call the parent class's withdraw method


# Encapsulated account class to demonstrate encapsulation
class EncapsulatedAccount:
    def __init__(self, balance=0.0):
        self.__balance = balance  # Private attribute to restrict direct access

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")

    # Method to access the private balance attribute safely
    def get_balance(self):
        return self.__balance


# Testing the combined functionality of all classes

# Create a general bank account
account = BankAccount("John Doe", 1000.0)
account.deposit(500)
account.withdraw(300)
print("Bank Account Balance:", account.get_balance())
print("-" * 40)

# Create a savings account and add interest
savings = SavingsAccount("Jane Doe", 2000.0, 0.03)
savings.add_interest()
print("Savings Account Balance after interest:", savings.get_balance())
print("-" * 40)

# Create a current account and attempt an overdraft
current = CurrentAccount("Paul Johnson", 500)
current.withdraw(600)  # Should show an overdraft warning
current.withdraw(400)  # Valid withdrawal
print("Current Account Balance:", current.get_balance())
print("-" * 40)

# Demonstrate encapsulation with a protected account
encap_account = EncapsulatedAccount(1000)
encap_account.deposit(300)
# Attempting to access private attribute directly would raise an error
# print(encap_account.__balance)  # Uncommenting this line would cause an AttributeError
print("Encapsulated Account Balance:", encap_account.get_balance())
