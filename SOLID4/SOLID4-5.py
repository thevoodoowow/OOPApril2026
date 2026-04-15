from abc import abstractmethod


class Charge:
    @abstractmethod
    def charge(self, amount: float):
        pass


class Refund:
    @abstractmethod
    def refund(self, transaction_id: str):
        pass


class Report:
    @abstractmethod
    def get_transaction_history(self) -> list:
        pass

    @abstractmethod
    def generate_report(self) -> str:
        pass


class BasicGateway(Charge):

    def charge(self, amount: float):
        print(f"Списание: {amount} руб.")


class FullGateway(Charge, Refund, Report):

    def charge(self, amount: float):
        print(f"Списание: {amount} руб.")

    def refund(self, transaction_id: str):
        print(f"Возврат по транзакции {transaction_id}")

    def get_transaction_history(self) -> list:
        return [{"id": "tx1", "amount": 500}]

    def generate_report(self) -> str:
        return "Отчёт: транзакций — 3"


def process_payment(gateway: Charge, amount: float):
    gateway.charge(amount)


def process_refunding(gateway: Refund, transaction_id: str):
    gateway.refund(transaction_id)


basic_gw = BasicGateway()
full_gw = FullGateway()

process_payment(basic_gw, 1500.0)
process_payment(full_gw, 2000.0)
process_refunding(full_gw, "tx123")
