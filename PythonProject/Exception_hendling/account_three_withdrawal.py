class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Account_Withdrawal:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, Current balance: {self.balance}")

    def withdraw(self, amount):
        # Check withdrawal limit first
        if self.count >= 3:
            raise InsufficientFundException(
                "You are not allowed more than 3 withdrawals"
            )

        # Check minimum balance rule
        if self.balance - amount < 2000:
            raise InsufficientFundException(
                "Insufficient funds! Minimum balance of 2000 required"
            )

        # If both conditions pass
        self.balance -= amount
        self.count += 1
        print(f"Withdrawn: {amount}, Current balance: {self.balance}")


# Example
ac = Account_Withdrawal()
ac.set_balance(10000)

try:
    ac.withdraw(2000)
    ac.withdraw(2000)
    ac.withdraw(2000)
    ac.withdraw(2000)
except InsufficientFundException as e:
    print("Exception:", e)
