from unittest import mock


@mock.patch("pdf_read.pdf_to_csv_handler.PdfToCsvHandler.run")
def test_run_called(mock_pdf_to_csv_handler, pdf_to_csv_handler):
    pdf_to_csv_handler.run()
    assert mock_pdf_to_csv_handler.called is True


def test_run(pdf_to_csv_handler, valid_contract):
    pdf_to_csv_handler.run(pdf_folder=valid_contract["folder"])


def test_extract_contract_details_from_folder(pdf_to_csv_handler, valid_contract):
    returned_value = pdf_to_csv_handler._extract_contract_details_from_folder(valid_contract["folder"])
    assert returned_value == [
        {"contract_number": "942739", "amount": "590.000,00", "date": "13/04/2021", "write_in_days": 100}
    ]


@mock.patch("pdf_read.pdf_to_csv_handler.PdfToCsvHandler._generate_csv")
def test_generate_csv(mock_generate_csv, pdf_to_csv_handler):
    pdf_to_csv_handler._generate_csv("path/fake", {"data": "fakse"})
    mock_generate_csv.assert_called_once_with("path/fake", {"data": "fakse"})


def test_transform_pdf_details_to_csv_details(pdf_to_csv_handler):
    contract_detail = {
        "contract_number": "736122",
        "amount": "1.400.000,00",
        "date": "15/02/2021",
        "write_in_days": 76,
    }
    response = pdf_to_csv_handler._transform_pdf_details_to_csv_details(contract_detail)
    assert response == {
        "Unit_id": "736122",
        "Valor_Total": "1.400.000,00",
        "Data_Contrato": "15/02/2021",
        "Data_escritura": "08/06/2021",
    }
