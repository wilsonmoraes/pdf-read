def test_get_amount(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_amount(valid_contract_content)
    assert "590.000,00" == returned_value


def test_get_amount_invalid(pdf_detail_handler):
    returned_value = pdf_detail_handler.get_amount([])
    assert "" == returned_value


def test_get_draw_up_in_days(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_count_deed_in_days(valid_contract_content)
    assert 100 == returned_value


def test_get_draw_up_in_days_invalid(pdf_detail_handler):
    returned_value = pdf_detail_handler.get_count_deed_in_days([])
    assert "" == returned_value


def test_get_contract_number(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_identifier(valid_contract_content)
    assert "942739" == returned_value


def test_get_contract_number_invalid(pdf_detail_handler):
    returned_value = pdf_detail_handler.get_identifier([])
    assert "" == returned_value


def test_get_contract_date(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_date(valid_contract_content)
    assert "13/04/2021" == returned_value


def test_get_contract_date_invalid(pdf_detail_handler, valid_contract_content):
    returned_value = pdf_detail_handler.get_date([])
    assert "" == returned_value
