from datetime import date
from unittest import mock

import pytest

from pdf_read.utils import find_following_working_day


@mock.patch("workalendar.america.BrazilBankCalendar.add_working_days")
def test_add_working_days(mocked_add_working_days):
    date_ = date(2020, 1, 1)
    find_following_working_day(date_, 2)
    mocked_add_working_days.assert_called_once_with(date_, 2)


@pytest.mark.parametrize(
    "current_date, working_days, expected_date",
    [
        (date(2021, 9, 4), 10, date(2021, 9, 20)),
        (date(2021, 11, 10), 16, date(2021, 12, 3)),
        (date(2021, 11, 10), 60, date(2022, 2, 4)),
        (date(2022, 11, 1), 15, date(2022, 11, 24)),
    ],
    ids=[
        "2 saturdays, 3 sundays, Independence Day",
        "3 saturdays, 3 sundays, Republic Proclamation",
        "13 saturdays, 13 sundays, Republic Proclamation, Christmas, New Year's",
        "3 saturdays, 3 sundays, All Souls', Republic Proclamation, Christmas",
    ],
)
def test_find_following_working_day(current_date, working_days, expected_date):
    assert find_following_working_day(current_date, working_days) == expected_date
