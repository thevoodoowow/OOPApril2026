class PaymentProcessor:
    def pay(self, payment_func, amount: float):
        payment_func(amount)


def pay_with_card(amount: float):
    print(f"Оплата картой: {amount} руб.")


def pay_with_crypto(amount: float):
    print(f"Оплата криптовалютой: {amount} руб.")


def pay_with_sbp(amount: float):
    print(f"Оплата через СБП: {amount} руб.")


processor = PaymentProcessor()

processor.pay(pay_with_card, 1500.0)
processor.pay(pay_with_crypto, 3200.0)
processor.pay(pay_with_sbp, 500.0)
