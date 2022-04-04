class User:
    def __init__(self, name):
        self.name = name
        self.account = {'retirement' : BankAccount(3, 100), 'personal' : BankAccount(1, 1000)}

    def withdrawal(self, amount, key):
        self.account[key].withdraw(amount)
        return self
    def deposit(self, amount, key):
        self.account[key].deposit(amount)
        return self
    def display_user_balance(self, key):
        print(f"User: {self.name}, Balance: {self.account[key].balance}")
    def transfer_money(self, user, amount, key):
        self.account[key].withdraw(amount)
        user.account[key].deposit(amount)
        return self

class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if self.balance >= 0:
            self.balance *= (1 + (self.int_rate/100))
            return self
        else:
            print("Your bank account is at a negative balance")

    @classmethod
    def print_instances(cls):
        for account in cls.all_accounts:
            print(account)

myself = User("Michael")
someone_else = User("Chad")

myself.deposit(100, 'retirement').display_user_balance('retirement')

