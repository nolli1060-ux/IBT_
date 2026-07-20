class Account:
    def _init_(self, owner, number, balance=0):
         self.owner = owner
         self.account_number = number
         self._balance = balance


    @property
    def balance(self):
        return self._balance
    
    def deposite (self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greaterthan 0")
        self._balance + amount 
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Insufficiet Balance")
        self._balance - amount

    def statement(self):
        print("Owner.", self.owner)
        print("Account Number.", self.account_number)
        print("Balance.", self._balance)