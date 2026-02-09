from abc import ABC, abstractmethod


class Payment(ABC):

    def process_payment(self, amount):
        fee = self.calculate_fee(amount)
        total = amount + fee
        return f"processing payment of {total}"

    @abstractmethod
    def calculate_fee(self, amount):
        pass


class CreditCardPayment(Payment):

    def calculate_fee(self, amount):
        return amount * 0.02


class UPIPayment(Payment):

    def calculate_fee(self, amount):
        return 0


class InternationalPayment(CreditCardPayment):

    def calculate_fee(self, amount):
        base_fee = super().calculate_fee(amount)
        return base_fee + 100


payments = [
    UPIPayment(),
    CreditCardPayment()
]

for payment in payments:
    print(payment.process_payment(1000))
