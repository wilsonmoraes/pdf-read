from unittest import mock


@mock.patch("pdf_read.pdf_to_csv_handler.PdfToCsvHandler.run")
def test_run_called(mock_pdf_to_csv_handler, pdf_to_csv_handler):
    pdf_to_csv_handler.run()
    assert mock_pdf_to_csv_handler.called is True


def test_run(pdf_to_csv_handler, valid_contract):
    pdf_to_csv_handler.run(pdf_folder=valid_contract["folder"])


def test_get_all_pdf_contents(pdf_to_csv_handler, valid_contract):
    returned_value = pdf_to_csv_handler._get_all_pdf_contents(valid_contract["folder"])
    assert len(returned_value) == 1
    assert "COMPROMISSO DE COMPRA E VENDA" in returned_value[0]


@mock.patch("pdf_read.pdf_to_csv_handler.PdfToCsvHandler._generate_csv")
def test_generate_csv(mock_generate_csv, pdf_to_csv_handler):
    pdf_to_csv_handler._generate_csv("path/fake", {"data": "fakse"})
    mock_generate_csv.assert_called_once_with("path/fake", {"data": "fakse"})


def test_transform_contract_info_to_csv_row(pdf_to_csv_handler, valid_contract_content):
    response = pdf_to_csv_handler._transform_contract_info_to_csv_row(valid_contract_content)
    assert response == {
        "Data_Contrato": "13/04/2021",
        "Data_escritura": "02/09/2021",
        "Unit_id": "942739",
        "Valor_Total": "590.000,00",
    }


def test_transform_contract_info_to_csv_row_failed(pdf_to_csv_handler):
    response = pdf_to_csv_handler._transform_contract_info_to_csv_row([])
    assert response == {"Unit_id": "", "Valor_Total": "", "Data_Contrato": "", "Data_escritura": ""}
