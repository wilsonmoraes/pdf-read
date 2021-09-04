from datetime import datetime

from workalendar.america import BrazilBankCalendar


def find_following_working_day(_date: datetime.date, working_days):
    cal = BrazilBankCalendar()
    return cal.add_working_days(_date, working_days)
