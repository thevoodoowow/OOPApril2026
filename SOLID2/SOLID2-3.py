from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass


class EmailChannel(NotificationChannel):
    def send(self, recipient: str, message: str):
        print(f"Email → {recipient}: {message}")


class SMSChannel(NotificationChannel):
    def send(self, recipient: str, message: str):
        print(f"SMS → {recipient}: {message}")


class NotificationService:
    def send(self, channel: NotificationChannel, recipient: str, message: str):
        channel.send(recipient, message)


class PushChannel(NotificationChannel):
    def send(self, recipient: str, message: str):
        print(f"Push → {recipient}: {message}")


service = NotificationService()

email = EmailChannel()
service.send(email, "user@example.com", "Ваш заказ подтверждён")

sms = SMSChannel()
service.send(sms, "+79001234567", "Код подтверждения: 1234")

push = PushChannel()
service.send(push, "user_id_45", "Новое уведомление в приложении")
