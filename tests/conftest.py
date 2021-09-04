import os

import pytest

from pdf_read.pdf_detail_handler import PdfDetailHandler
from pdf_read.pdf_to_csv_handler import PdfToCsvHandler


@pytest.fixture
def pdf_detail_handler():
    return PdfDetailHandler()


@pytest.fixture
def pdf_to_csv_handler():
    return PdfToCsvHandler()


@pytest.fixture
def valid_contract():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return {"folder": f"{root_dir}/data", "file_name": "valid_contract.pdf"}


@pytest.fixture
def valid_contract_content():
    return [
        "COMPROMISSO DE COMPRA E VENDA ",
        "EDIFÍCIO LOFT ",
        "Rua Tabapuã, nº 745, Itaim. ",
        "942739 ",
        "SP - SÃO PAULO ",
        "3. Do Valor da Compra e Venda ",
        "3.1. R$ 590.000,00 ( oitocentos mil reais) ",
        "4. Da Forma de Pagamento do Valor da Compra e Venda ",
        "referente a ausência de pagamentos em favor de MARIA SILVA. ",
        "5. Da Escritura de Compra e Venda ",
        "A Escritura deverá ser lavrada em até 100 (cem) dias corridos contados da assinatura do ",
        "Compromisso, desde que o VENDEDOR apresente todos os documentos e/ou esclarecimentos ",
        "b) Apresentação de esclarecimentos adicionais (se aplicável): em até 5 (cinco) dias úteis após a ",
        "solicitação. ",
        "São Paulo, 13/04/2021 ",
    ]


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
