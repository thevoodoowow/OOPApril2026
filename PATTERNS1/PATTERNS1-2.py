from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def generate(self, data: dict) -> str:
        pass


class PdfReport(Report):
    def generate(self, data: dict) -> str:
        return f"[PDF] Отчёт: {data}"


class ExcelReport(Report):
    def generate(self, data: dict) -> str:
        return f"[Excel] Отчёт: {data}"


class CsvReport(Report):
    def generate(self, data: dict) -> str:
        return f"[CSV] Отчёт: {data}"


class ReportManager(ABC):
    @abstractmethod
    def create_generator(self) -> Report:
        pass

    def export(self, data: dict) -> str:
        generator = self.create_generator()
        return generator.generate(data)


class PdfReportManager(ReportManager):
    def create_generator(self) -> Report:
        return PdfReport()


class ExcelReportManager(ReportManager):
    def create_generator(self) -> Report:
        return ExcelReport()


class CsvReportManager(ReportManager):
    def create_generator(self) -> Report:
        return CsvReport()


manager = PdfReportManager()
print(manager.export({"title": "Продажи Q1", "total": 150000}))

manager_excel = ExcelReportManager()
print(manager_excel.export({"title": "Продажи Q1", "total": 150000}))
