import os

import pytest

from pdf_read.pdf_detail_handler import PdfDetailHandler


@pytest.fixture
def pdf_detail_handler():
    return PdfDetailHandler()


@pytest.fixture
def valid_contract():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return {"folder": f"{root_dir}/data", "file_name": "valid_contract.pdf"}


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
