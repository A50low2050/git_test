from abc import ABC, abstractmethod
from typing import Any
from urllib.parse import ParseResult


class ReportGeneration(ABC):

    @abstractmethod
    def generate_report(self):
        pass


class ReportSaver(ABC):
    @abstractmethod
    def save_report(self, report: Any):
        pass


class CSV(ReportGeneration):

    def __init__(self, data):
        self.data = data

    def generate_report(self):
        print("Generating CSV report...")
        return self.data


class PDF(ReportGeneration):
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        print("Generating PDF report...")
        return self.data


class EXEL(ReportGeneration):
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        print("Generating EXEL report...")
        return self.data


class FileSaver(ReportSaver):
    def save_report(self, report: ReportGeneration):
        print(f"Saving data {report} report...")

class ReportProcessor:
    def __init__(self, generation: ReportGeneration, saver: ReportSaver):
        self.generation = generation
        self.saver = saver

    def process(self):
        report = self.generation.generate_report()
        self.saver.save_report(report)
        return report

saver = FileSaver()

csv_processor = ReportProcessor(CSV(["csv_data"]), saver)
pdf_processor = ReportProcessor(PDF(["pdf_data"]), saver)
excel_processor = ReportProcessor(EXEL(["excel_data"]), saver)

csv_result = csv_processor.process()
pdf_result = pdf_processor.process()
excel_result = excel_processor.process()




