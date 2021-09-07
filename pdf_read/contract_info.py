import re


class ContractInfo:
    @staticmethod
    def get_identifier(content: [str]):
        try:
            return content[3].strip()
        except (IndexError, ValueError):
            return ""

    @staticmethod
    def get_amount(content: [str]):
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

    @staticmethod
    def get_count_deed_in_days(content: [str]):
        try:
            count_deed_in_days = next(
                filter(lambda x: x.startswith("A Escritura deverá ser lavrada"), content)
            )
            return int(re.search(r"\d+", count_deed_in_days).group())
        except (IndexError, ValueError, StopIteration):
            return ""

    @staticmethod
    def get_date(content: [str]):
        try:
            return re.search(r"([0-9]{2}\/[0-9]{2}\/[0-9]{4})", content[-1]).group()
        except (IndexError, ValueError):
            return ""
