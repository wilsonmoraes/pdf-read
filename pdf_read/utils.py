from datetime import datetime

from workalendar.america import BrazilBankCalendar


def find_following_working_day(date: datetime.date, working_days):
    cal = BrazilBankCalendar()
    return cal.add_working_days(date, working_days)
