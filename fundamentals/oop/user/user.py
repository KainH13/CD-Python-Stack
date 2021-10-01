class User:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        print(f"{self.username} made a desposit of ${amount}")
        return self
    
    def make_withdrawal(self, amount):
        self.balance -= amount
        print(f"{self.username} made a withdrawal of ${amount}")
        return self

    def display_user_balance(self):
        print(f"User: {self.username}, Balance: ${self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        print(f"{self.username} transferred ${amount} to {other_user.username}")
        return self

user1 = User("Guido", 1000000)
user2 = User("Kai", 200000)
user3 = User("Ariel", 500000)

user1.display_user_balance().make_deposit(500).display_user_balance().make_withdrawal(1000).display_user_balance().transfer_money(user3, 3000).display_user_balance()
user2.display_user_balance()
user3.display_user_balance()