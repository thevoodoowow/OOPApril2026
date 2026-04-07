from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    id: str
    price: float
    qty: int
    customer_email: str

    @property
    def total_cost(self) -> float:
        return self.price * self.qty


import json
class OrderLoader:
    def load_from_file(self, putb: str) -> list[Order]:
        with open(putb, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [self._parse_item(item) for item in data]

    def _parse_item(self, item: dict) -> Order:

        required = ["id", "price", "qty", "email"]
        if not all(k in item for k in required):
            raise ValueError(f"Missing fields in: {item}")

        if int(item["qty"]) <= 0:
            raise ValueError(f"Invalid quantity: {item['qty']}")

        return Order(
            id=item["id"],
            price=float(item["price"]),
            qty=int(item["qty"]),
            customer_email=item["email"],
        )


class Calculator:
    def get_total_sum(self, orders: list[Order]) -> float:
        return sum(o.total_cost for o in orders)

class Formatter:
    def format_text(self, orders: list[Order], total_sum: float) -> str:
        return f"Orders count: {len(orders)}\n" f"Total: {total_sum:.2f}\n"

from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def notify(self, recipient: str, message: str):
        pass

class EmailNotifier(Notification):
    def notify(self, recipient: str, message: str):
        print(f"[EMAIL to={recipient}] Your order report\n{message}")

class ConsoleNotifier(Notification):
    def notify(self, recipient: str, message: str):
        print(f"[LOG] Sent to {recipient}")

class OrderReportManager:
    def __init__(
        self,
        loader: OrderLoader,
        calculator: Calculator,
        formatter: Formatter,
        notifier: Notification,
    ):
        self.loader = loader
        self.calculator = calculator
        self.formatter = formatter
        self.notifier = notifier

    def process(self, fileputb: str):

        orders = self.loader.load_from_file(fileputb)

        total = self.calculator.get_total_sum(orders)

        report_content = self.formatter.format_text(orders, total)

        for order in orders:
            self.notifier.notify(order.customer_email, report_content)
        return report_content

manager = OrderReportManager(
    loader=OrderLoader(),
    calculator=Calculator(),
    formatter=Formatter(),
    notifier=EmailNotifier()
)
manager.process("orders.json")

class MockNotifier(Notification):
    def notify(self, r, m): pass

silent_manager = OrderReportManager(OrderLoader(), Calculator(), Formatter(), MockNotifier())
