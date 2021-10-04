class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
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


class User:
    def __init__(self, username, int_rate=0.2, balance=0):
        self.username = username
        self.account = BankAccount(int_rate, balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"{self.username} made a desposit of ${amount}")
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(f"{self.username} made a withdrawal of ${amount}")
        return self

    def display_user_balance(self):
        print(f"User: {self.username}, Balance: ${self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        print(f"{self.username} transferred ${amount} to {other_user.username}")
        return self


user1 = User("Guido", 0.2, 1000000)
user2 = User("Kai", 0.5, 200000)
user3 = User("Ariel", 0.4, 500000)

user1.display_user_balance().make_deposit(500).display_user_balance().make_withdrawal(1000).display_user_balance().transfer_money(user3, 3000).display_user_balance()
user2.display_user_balance()
user3.display_user_balance()