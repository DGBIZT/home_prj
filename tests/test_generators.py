import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency():
    expected_result = [
        {
            "id": 129309161,
            "date": "2018-09-26T00:46:36.256087",
            "operationAmount": {"amount": "17250", "currency": {"code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1313132313442324",
            "to": "Счет 1743370781324891402",
        },
        {
            "id": 129309161,
            "date": "2018-09-26T00:46:36.256087",
            "operationAmount": {"amount": "17250", "currency": {"code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1313132313442324",
            "to": "Счет 1743370781324891402",
        },
    ]
    result = list((x for x in expected_result if x["operationAmount"]["currency"]["code"] == "USD"))
    for item in result:
        yield item
    assert filter_by_currency == result
