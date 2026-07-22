# DAY 5 CODE 
class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self._Account__balance = balance

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
        
        # Check if the amount exceeds the balance PLUS the allowed overdraft limit
        if amount > (self.balance + self.overdraft):
            raise ValueError("Overdraft limit exceeded")
            
        # Since __balance is private to the parent class, I modify it using Python's name mangling
        self._Account__balance -= amount

    # TODO: override statement() to label the account type
    def statement(self):
        print("--- Current Account ---")
        super().statement()

# Polymorphic Loop 
print("--- Creating Accounts ---")
savings = SavingsAccount("Matiyas", "100077222209", 1000, 0.05)
current = CurrentAccount("Getachew", "100017828337", 200, 500)

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


# DAY 6 CODE

def subscribe(self, observer):
    if not hasattr(self, "_observers"):
        self._observers = []
    self._observers.append(observer)

def _notify(self, event):
    if hasattr(self, "_observers"):
        for observer in self._observers:
            observer.update(event)

Account.subscribe = subscribe
Account._notify = _notify

_orig_deposit = Account.deposit
def _deposit_with_notify(self, amount):
    _orig_deposit(self, amount)
    self._notify(f"+{amount} ETB to {self.account_number}")

_orig_withdraw_current = CurrentAccount.withdraw
def _withdraw_with_notify_current(self, amount):
    _orig_withdraw_current(self, amount)
    self._notify(f"-{amount} ETB from {self.account_number}")

Account.deposit = _deposit_with_notify
CurrentAccount.withdraw = _withdraw_with_notify_current

class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        if kind == "current":
            return CurrentAccount(owner, number, balance)
        raise ValueError(f"Unknown type: {kind}")


class SMSAlert:
    def update(self, event):
        print(f"[CBE SMS] {event}")


class AuditLog:
    def update(self, event):
        print(f"[Log] {event}")


