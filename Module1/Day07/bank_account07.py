class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self._Account__balance = balance
        self.history = []

    @property
    def balance(self):
        return self._Account__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._Account__balance += amount
    
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._Account__balance:
            raise ValueError("Insufficient funds")
        self._Account__balance -= amount
        self.history.append(("withdraw", amount))

    
    def undo_last(self):
        if not self.history:
            print(f"[{self.account_number}] No transactions to undo.")
            return

        action, amount = self.history.pop() 

        if action == "deposit":
            self._Account__balance -= amount
            print(f"[{self.account_number}] Undid Deposit of {amount} ETB. Balance: {self.balance} ETB")
        elif action == "withdraw":
            self._Account__balance += amount
            print(f"[{self.account_number}] Undid Withdrawal of {amount} ETB. Balance: {self.balance} ETB")

    def statement(self):
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)

    def statement(self):
        print("--- Savings Account ---")
        super().statement()


class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > (self.balance + self.overdraft):
            raise ValueError("Overdraft limit exceeded")
        
        self._Account__balance -= amount
        self.history.append(("withdraw", amount))

    def statement(self):
        print("--- Current Account ---")
        super().statement()


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


class AccountRegistry:
    def __init__(self):
        self.accounts = {}

    def add(self, account):
        """O(1) Insert - add account to registry"""
        self.accounts[account.account_number] = account
        print(f"[Registry] Added account {account.account_number} for {account.owner}")

    def find(self, number):
        """O(1) Lookup by Key - retrieve account by number"""
        return self.accounts.get(number)

    def list_all(self):
        """O(n) Ordered List Generation - return all accounts"""
        return list(self.accounts.values())


if __name__ == "__main__":
    print("=" * 50)
    print("DAY 07: AccountRegistry with Transaction History")
    print("=" * 50)
    
    sms = SMSAlert()
    audit = AuditLog()

    registry = AccountRegistry()

    print("\n--- 1. Creating Accounts via Factory ---")
    acc1 = AccountFactory.create("savings", "Matiyas", "100077222209", 1000)
    acc2 = AccountFactory.create("current", "Getachew", "100017828337", 200)

    for acc in [acc1, acc2]:
        acc.subscribe(sms)
        acc.subscribe(audit)

    print("\n--- 2. Adding to Registry (O(1) Operation) ---")
    registry.add(acc1)
    registry.add(acc2)

    print("\n--- 3. Testing O(1) Find in Registry ---")
    found_acc = registry.find("100077222209")
    if found_acc:
        print(f"✓ Found account for: {found_acc.owner}\n")

    print("--- 4. Performing Transactions ---")
    found_acc.deposit(500)
    found_acc.deposit(200)

    print("\n--- 5. Testing Undo Stack (O(1) Pop) ---")
    found_acc.undo_last() 
    found_acc.undo_last() 

    print("\n--- 6. Final Account Statement ---")
    found_acc.statement()
    print(f"Transaction History: {found_acc.history}")

    print("\n--- 7. Listing All Accounts in Registry ---")
    for acc in registry.list_all():
        acc.statement()
        print()
