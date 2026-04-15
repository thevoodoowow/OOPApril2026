from abc import abstractmethod


class Notifier:
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass


class EmailSender(Notifier):
    def send(self, recipient: str, message: str):
        print(f"Email → {recipient}: {message}")


class SmsSender(Notifier):
    def send(self, recipient: str, message: str):
        print(f"SMS → {recipient}: {message}")


class OrderService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def place_order(self, order_id: int, contact: str):
        print(f"Заказ #{order_id} оформлен")
        self.notifier.send(contact, f"Ваш заказ #{order_id} принят")


email_service = OrderService(EmailSender())
email_service.place_order(101, "user@example.com")

sms_service = OrderService(SmsSender())
sms_service.place_order(102, "88005553535")
