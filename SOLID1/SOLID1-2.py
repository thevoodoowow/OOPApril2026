class SalesReport:

    def __init__(self, data: list[dict]):
        self.data = data

    def get_total(self) -> float:
        return sum(item["amount"] for item in self.data)


class HTMLFormatter:

    @staticmethod
    def render_html(report: SalesReport) -> str:
        rows = "".join(
            f"<tr><td>{d['name']}</td><td>{d['amount']}</td></tr>" for d in report.data
        )
        total = report.get_total()
        return f"<table>{rows}<tr><td>Итого</td><td>{total}</td></tr></table>"


report = SalesReport(
    [
        {"name": "Товар A", "amount": 1500},
        {"name": "Товар B", "amount": 2300},
    ]
)
html_output = HTMLFormatter.render_html(report)
print(html_output)
