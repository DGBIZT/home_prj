import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

@pytest.mark.parametrize("currency, id_transactions", [("USD", 129309161), ("RUB", 999888555)])
def test_filter_by_currency(transaction, currency, id_transactions):

    filtred_transactions = filter_by_currency(transaction, currency)
    assert next(filtred_transactions)["id"] == id_transactions

def test_filter_by_currency_1():
    with pytest.raises(ValueError, match="Ваш список пуст, заполните его"):
        list(filter_by_currency([],"USD"))

def test_filter_by_currency_error_2(transaction_rub):
    with pytest.raises(TypeError):
        list(filter_by_currency(transaction_rub,"USD"))


def test_transaction_descriptions(transaction_descriptions_mylist):
    result = next(transaction_descriptions(transaction_descriptions_mylist))
    assert result == "Перевод с карты на счет"


def test_card_number_generator():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"

