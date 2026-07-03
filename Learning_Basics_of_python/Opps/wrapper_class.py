class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print("Remaining:", self.balance)

class SecureBankAccount:

    def __init__(self, account):
        self.account = account

    def withdraw(self, amount):

        if amount > self.account.balance:
            print("Insufficient Balance")
        else:
            print("Transaction Started")
            self.account.withdraw(amount)
            print("Transaction Completed")

acc = BankAccount(5000)
secure = SecureBankAccount(acc)
secure.withdraw(500)
secure.withdraw(1000)

