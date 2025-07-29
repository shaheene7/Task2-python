from abc import ABC, abstractmethod

class Stripe:
    def __init__(self):
        self.gateway = "stripe"

    def charge(self, amount):
        print(f"Charging ${amount} with Stripe")

class PayPal:
    def __init__(self):
        self.gateway = "paypal"

    def charge(self, amount):
       print(f"Processing ${amount} with PayPal")

class local:
    def __init__(self):
        self.gateway = "local"

    def charge(self, amount):
        print(f"Handling ${amount} with LocalBankAPI")


class PaymentProcessor(ABC):
    @abstractmethod
    def charge(self, amount):
        pass

class StripeAdapter(PaymentProcessor):
    def __init__(self):
        self.gateway = Stripe()

    def charge(self, amount):
        self.gateway.charge(amount)

class PayPalAdapter(PaymentProcessor):
    def __init__(self):
        self.gateway = PayPal()

    def charge(self, amount):
        self.gateway.charge(amount)

class LocalBankAdapter(PaymentProcessor):
    def __init__(self):
        self.gateway = local()

    def charge(self, amount):
        self.gateway.charge(amount)

def get_payment_processor(gateway):
    if gateway == "stripe":
        return StripeAdapter()
    elif gateway == "paypal":
        return PayPalAdapter()
    elif gateway == "local":
        return LocalBankAdapter()
    else:
        raise ValueError("Unsupported payment gateway")
    



processor = get_payment_processor("stripe")
processor.charge(100)

processor = get_payment_processor("paypal")
processor.charge(200)

processor = get_payment_processor("local")
processor.charge(300)

""" it allows different payment gateways to be used through a common PaymentProcessor 
    This promotes flexibility and reuse as new gateways can be integrated simply by writing a small adapter class"""