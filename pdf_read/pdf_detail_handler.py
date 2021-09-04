import re

from pdfminer.high_level import extract_text


class PdfDetailHandler:
    def get_detail(self, pdf_path):
        content = extract_text(pdf_path)
        content = [s for s in content.splitlines() if s]
        return {
            "contract_number": self.get_contract_number(content),
            "amount": self.get_amount(content),
            "date": self.get_contract_date(content),
            "write_in_days": self.get_draw_up_in_days(content),
        }

    def get_amount(self, content: [str]):
        try:
            amount = list(filter(lambda x: x.startswith("3.1."), content))[0]
            return re.findall(
                r"""
                    ([.]?\d[\d\s.,]*)   # number, probably with thousand separators
                    \s*?                # skip whitespace
                    """,
                amount,
                re.VERBOSE,
            )[1].strip()
        except (IndexError, ValueError):
            return ""

    def get_draw_up_in_days(self, content: [str]):
        try:
            write_in_days = next(filter(lambda x: x.startswith("A Escritura deverá ser lavrada"), content))
            return int(re.search(r"\d+", write_in_days).group())
        except (IndexError, ValueError):
            return ""

    def get_contract_number(self, content: [str]):
        try:
            return content[3].strip()
        except (IndexError, ValueError):
            return ""

    def get_contract_date(self, content: [str]):
        try:
            return re.search(r"([0-9]{2}\/[0-9]{2}\/[0-9]{4})", content[-1]).group()
        except (IndexError, ValueError):
            return ""
