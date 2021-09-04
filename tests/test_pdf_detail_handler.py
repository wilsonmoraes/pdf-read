import pytest


def test_get_detail_success(pdf_detail_handler, valid_contract):
    returned_value = pdf_detail_handler.get_detail(
        f"{valid_contract['folder']}/{valid_contract['file_name']}"
    )
    assert returned_value == {
        "contract_number": "942739",
        "amount": "590.000,00",
        "date": "13/04/2021",
        "write_in_days": 100,
    }


def test_get_detail_file_not_found(pdf_detail_handler, valid_contract):
    with pytest.raises(FileNotFoundError) as exc:
        pdf_detail_handler.get_detail(f"{valid_contract['folder']}/fake.pdf")
    assert exc.type == FileNotFoundError
    assert "No such file" in str(exc)


def test_get_amount(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_amount(valid_contract_content)
    assert "590.000,00" == returned_value


def test_get_amount_invalid(pdf_detail_handler):
    returned_value = pdf_detail_handler.get_amount([])
    assert "" == returned_value


def test_get_draw_up_in_days(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_draw_up_in_days(valid_contract_content)
    assert 100 == returned_value


def test_get_draw_up_in_days_invalid(pdf_detail_handler):
    returned_value = pdf_detail_handler.get_draw_up_in_days([])
    assert "" == returned_value


def test_get_contract_number(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_contract_number(valid_contract_content)
    assert "942739" == returned_value


def test_get_contract_number_invalid(pdf_detail_handler):
    returned_value = pdf_detail_handler.get_contract_number([])
    assert "" == returned_value


def test_get_contract_date(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_contract_date(valid_contract_content)
    assert "13/04/2021" == returned_value


def test_get_contract_date_invalid(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_contract_date([])
    assert "" == returned_value
