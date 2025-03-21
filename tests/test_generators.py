import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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
            "id": 999888555,
            "date": "2025-03-19T10:3:58.027767",
            "operationAmount": {"amount": "250", "currency": {"code": "USD"}},
            "description": "Перевод организации STMU",
            "from": "Счет - 63475662387234505765",
            "to": "Счет 8175128657841941437",
        },
    ]
    transactions = [
        {
            "id": 129309161,
            "date": "2018-09-26T00:46:36.256087",
            "operationAmount": {"amount": "17250", "currency": {"code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1313132313442324",
            "to": "Счет 1743370781324891402",
        },
        {
            "id": 999888555,
            "date": "2025-03-19T10:3:58.027767",
            "operationAmount": {"amount": "250", "currency": {"code": "USD"}},
            "description": "Перевод организации STMU",
            "from": "Счет - 63475662387234505765",
            "to": "Счет 8175128657841941437",
        },
    ]

    result = list(
        (x for x in filter_by_currency(transactions, "USD") if x["operationAmount"]["currency"]["code"] == "USD")
    )
    for item in result:
        assert item in expected_result
    with pytest.raises(TypeError):
        filter_by_currency("")
    with pytest.raises(TypeError):
        filter_by_currency([])
    with pytest.raises(TypeError):
        filter_by_currency(0)


def test_transaction_descriptions(transaction_descriptions_mylist):
    result = next(transaction_descriptions(transaction_descriptions_mylist))
    assert result == "Перевод с карты на счет"


def test_card_number_generator():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
