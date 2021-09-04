import glob
import re

from config import settings
from pdfminer.high_level import extract_text


class ExtractPdfInfoHandler:
    def get_all_contract_details(self):
        pdfs = glob.glob(f"{settings.READ_PDFS_FROM_FOLDER}/*.pdf")
        return [self.get_contract_detail(pdf) for pdf in pdfs]

    def get_contract_detail(self, pdf_path):
        content = extract_text(pdf_path)
        content = [s for s in content.splitlines() if s]
        return {
            "contract_number": self.get_contract_number(content),
            "amount": self.get_amount(content),
            "write_in_days": self.get_draw_up_in_days(content),
            "date": self.get_contract_date(content),
        }

    def get_amount(self, content: [str]):
        amount = list(filter(lambda x: x.startswith("3.1."), content))[0]
        return re.findall(
            r"""
                ([.]?\d[\d\s.,]*)   # number, probably with thousand separators
                \s*?                # skip whitespace
                """,
            amount,
            re.VERBOSE,
        )[1]

    def get_draw_up_in_days(self, content: [str]):
        write_in_days = next(filter(lambda x: x.startswith("A Escritura deverá ser lavrada"), content))
        return int(re.search(r"\d+", write_in_days).group())

    def get_contract_number(self, content: [str]):
        return content[3].strip()

    def get_contract_date(self, content: [str]):
        return re.search(r"([0-9]{2}\/[0-9]{2}\/[0-9]{4})", content[-1]).group()
