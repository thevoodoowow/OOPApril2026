class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class EmailValidator:
    @staticmethod
    def is_valid(email: str) -> bool:
        return "@" in email


class EmailService:
    def send_welcome(self, user: User):
        print(f"Отправка на {user.email}: Добро пожаловать, {user.name}!")


user = User("Алексей", "alex@example.com")

if EmailValidator.is_valid(user.email):
    service = EmailService()
    service.send_welcome(user)
