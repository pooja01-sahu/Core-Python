class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Account_Withdrawal:
    def __init__(self):
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"deposited:,{amount}, current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= 2000:
            self.balance -= amount
            print(f"withdrawn:,{amount}, current balance: {self.balance}")
        else:
            raise InsufficientFundException("Insufficient funds")



    # Example
ac = Account_Withdrawal()
ac.set_balance(5000)

try:
    ac.deposit(2000)
    ac.withdraw(3000)
    ac.withdraw(2500)
except InsufficientFundException as e:
    print("exception", e)
