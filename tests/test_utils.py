from datetime import date
from unittest import mock

from pdf_read.utils import find_following_working_day


@mock.patch("workalendar.america.BrazilBankCalendar.add_working_days")
def test_find_following_working_day(mocked_add_working_days):
    date_ = date(2020, 1, 1)
    find_following_working_day(date_, 2)
    mocked_add_working_days.assert_called_once_with(date_, 2)
