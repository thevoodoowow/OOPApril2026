from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotification(Notification):
    def __init__(self, address: str):
        self.address = address

    def send(self, message: str):
        print(f"Email → {self.address}: {message}")


class SmsNotification(Notification):
    def __init__(self, phone: str):
        self.phone = phone

    def send(self, message: str):
        print(f"SMS → {self.phone}: {message}")


class PushNotification(Notification):
    def __init__(self, device_token: str):
        self.device_token = device_token

    def send(self, message: str):
        print(f"Push → {self.device_token}: {message}")


class Notifier(ABC):
    @abstractmethod
    def create_notification(self, target: str) -> Notification:
        pass

    def notify(self, target: str, message: str):
        notification = self.create_notification(target)
        notification.send(message)


class EmailNotifier(Notifier):
    def create_notification(self, target: str) -> Notification:
        return EmailNotification(target)


class SmsNotifier(Notifier):
    def create_notification(self, target: str) -> Notification:
        return SmsNotification(target)


class PushNotifier(Notifier):
    def create_notification(self, target: str) -> Notification:
        return PushNotification(target)


def client_code(notifier: Notifier, target: str, message: str):
    notifier.notify(target, message)


client_code(EmailNotifier(), "user@example.com", "Ваш заказ подтверждён")
client_code(SmsNotifier(), "+79001234567", "Код подтверждения: 1234")
