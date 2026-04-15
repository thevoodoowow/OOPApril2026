class Account:
    def __init__(self, name: str):
        self.name = name


class UserAccount(Account):
    def get_discount(self) -> float:
        return 0.10


class PremiumAccount(Account):
    def get_discount(self) -> float:
        return 0.25


class GuestAccount(Account):
    pass


def print_discounts(accounts: list[Account]):
    for acc in accounts:
        print(f"{acc.name}: скидка {acc.get_discount() * 100}%")


# Вызов
accounts = [UserAccount("Анна"), PremiumAccount("Иван")]
print_discounts(accounts)
