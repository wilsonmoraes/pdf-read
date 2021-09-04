def test_get_detail_success(pdf_detail_handler, valid_contract):
    returned_value = pdf_detail_handler.get_detail(
        f"{valid_contract['folder']}/{valid_contract['file_name']}"
    )
    assert returned_value == {
        "contract_number": "942739",
        "amount": "590.000,00 ",
        "date": "13/04/2021",
        "write_in_days": 100,
    }
