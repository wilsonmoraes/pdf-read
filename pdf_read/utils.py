from datetime import datetime

from pdfminer.high_level import extract_text
from workalendar.america import BrazilBankCalendar


def find_following_working_day(date: datetime.date, working_days):
    """
    Return next following working day accord numbers of working days

    Parameters:
        date (date):referenced date.
        working_days: number of days to sum

    Returns:
        date:The next following work day.
    """
    cal = BrazilBankCalendar()
    return cal.add_working_days(date, working_days)


def pdf_content_to_str(pdf_path) -> [str]:
    """
    Return all content of pdf as str list

    Parameters:
        pdf_path (str):The string which is to be reversed.

    Returns:
        [str]:The string which gets reversed.
    """
    content = extract_text(pdf_path)
    return [s.strip() for s in content.splitlines() if s]
