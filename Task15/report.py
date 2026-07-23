from abc import ABC, abstractmethod

# Abstract Base Class
class Report(ABC):
    def __init__(self, title):
        self._title = title  

    def show_header(self):
        return f"{self._title} Report Header"

    # Abstract method
    @abstractmethod
    def generate(self):
        pass


# Subclass 1: PDFReport
class PDFReport(Report):
    def __init__(self, title, page_size):
        super().__init__(title)
        self.__page_size = page_size

    def generate(self):
        header = super().show_header()
        print(f"Generating PDF content :[Page Size: {self.__page_size}]")
        print("PDF Report generation complete.\n")


# Subclass 2: HTMLReport
class HTMLReport(Report):
    def __init__(self, title, theme):
        super().__init__(title)
        self.__theme = theme

    def generate(self):
        header = super().show_header()
        print(f"Generating HTML layout: [Theme: {self.__theme}]")
        print("HTML Report generation complete.\n")


pdf_doc = PDFReport("Q3 Financials", "A4")
html_doc = HTMLReport("User Analytics", "Dark Mode")

pdf_doc.generate()
html_doc.generate()
