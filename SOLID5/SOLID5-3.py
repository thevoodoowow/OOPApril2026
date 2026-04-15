from abc import abstractmethod


class Render:
    @abstractmethod
    def render(self, content: str) -> str:
        pass


class PdfRender(Render):
    def render(self, content: str) -> str:
        return f"[PDF] {content}"


class HtmlRender(Render):
    def render(self, content: str) -> str:
        return f"<html><body>{content}</body></html>"


class ReportGenerate:
    def __init__(self, renderer: Render):
        self.renderer = renderer

    def generate(self, data: str) -> str:
        content = f"Отчёт: {data}"
        return self.renderer.render(content)


pdf_gen = ReportGenerate(PdfRender())
print(pdf_gen.generate("Продажи за март"))

html_gen = ReportGenerate(HtmlRender())
print(html_gen.generate("Продажи за март"))
