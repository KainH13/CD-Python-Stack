class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def desposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print(f"Insufficient funds (balance: ${self.balance}): Charging a $5 fee")
            self.balance -= 5
            print(f"Balance now ${self.balance}")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance} \nInterest Rate: {self.int_rate}")
        return self

    def yield_interest(self):
        print(f"Applying interest to balance of ${self.balance}...")
        self.balance += self.balance * self.int_rate
        print(f"New balance: ${self.balance}")
        return self

    @classmethod
    def all_info(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance} Interest Rate: {account.int_rate}")

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


account1 = BankAccount(0.05, 1000000)
account2 = BankAccount(0.80)

account1.desposit(1000).desposit(1000).desposit(3000).withdraw(50000).yield_interest().display_account_info()
account2.desposit(50000).desposit(50000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info()

BankAccount.all_info()