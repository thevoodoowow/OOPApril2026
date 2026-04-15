from abc import abstractmethod


class Printer:
    @abstractmethod
    def print_doc(self, document: str):
        pass


class Scanner:
    @abstractmethod
    def scan_doc(self, document: str):
        pass


class Fax:
    @abstractmethod
    def send_fax(self, document: str):
        pass


class SimplePrinter(Printer):
    def print_doc(self, document: str):
        print(f"Печать: {document}")


class AdvancedPrinter(Printer, Scanner, Fax):
    def print_doc(self, document: str):
        print(f"Печать: {document}")

    def scan_doc(self, document: str):
        print(f"Сканирование: {document}")

    def send_fax(self, document: str):
        print(f"Отправка факса: {document}")


def copy_document(printer: Printer, scanner: Scanner, doc: str):
    scanner.scan_doc(doc)
    printer.print_doc(doc)


simple = SimplePrinter()
advanced = AdvancedPrinter()

simple.print_doc("Отчет.pdf")
advanced.scan_doc("Квартальный отчет")
