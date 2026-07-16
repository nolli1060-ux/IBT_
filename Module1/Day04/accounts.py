# Base Account Class (From Day 4 Slide)
class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def statement(self):
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance)


class SavingsAccount(Account):
    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)

    # TODO: override statement to label the account type
    def statement(self):
        print("--- Savings Account ---")
        super().statement()


# CurrentAccount 
class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    # TODO: override withdraw() to allow the overdraft
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Check if the amount exceeds your balance PLUS the allowed overdraft limit
        if amount > (self.balance + self.overdraft):
            raise ValueError("Overdraft limit exceeded")
            
        # Since __balance is private to the parent class, I modify it using Python's name mangling
        self._Account__balance -= amount

    # TODO: override statement() to label the account type
    def statement(self):
        print("--- Current Account ---")
        super().statement()


# Step 5: Polymorphic Loop 
print("--- Creating Accounts ---")
savings = SavingsAccount("Matiyas", "SAV-2001", 1000, 0.05)
current = CurrentAccount("Getachew", "CUR-3001", 200, 500)

# specific features
savings.add_interest()
current.withdraw(400) # Uses 200 from balance and 200 from overdraft

print("\n--- Driving via Polymorphic Loop ---")
# Create a mixed list of different account objects
accounts = [savings, current]

# Loop through them all and call statement()
for acc in accounts:
    acc.statement()
    print()  # Prints an empty line between accounts