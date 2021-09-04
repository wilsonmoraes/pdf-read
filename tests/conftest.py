import pytest


@pytest.fixture
def pdf_details_data():
    return [
        {
            "contract_number": "736122",
            "amount": "1.400.000,00 ",
            "date": "15/02/2021",
            "write_in_days": 76,
        },
        {
            "contract_number": "942739",
            "amount": "590.000,00 ",
            "date": "13/04/2021",
            "write_in_days": 100,
        },
        {
            "contract_number": "592837",
            "amount": "800.000,00 ",
            "date": "17/03/2021",
            "write_in_days": 100,
        },
    ]
