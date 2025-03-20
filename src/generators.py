from typing import Any, Generator, Iterator


def filter_by_currency(transaction: list[dict[str, int | str]], forex: str) -> Iterator[list[dict[str, int | str]]]:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции"""

    if transaction == []:
        raise UnboundLocalError("Ваш список пуст, заполните его")
    elif forex == "":
        raise TypeError("Введите валюту для получения информации")
    for _ in range(len(transactions)):
        total_number = 0
        for item in transactions:
            if item["operationAmount"]["currency"]["code"] != forex:
                total_number += 1
    if total_number == len(transactions):
        raise ValueError("По данной валюте нет транзакций!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        currency_code = list((x for x in transaction if x["operationAmount"]["currency"]["code"] == forex))
        for item in currency_code:
            yield item


transactions = [
    {
        "id": 970157810,
        "date": "2018-06-08T10:3:58.027767",
        "operationAmount": {"amount": "150", "currency": {"code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет - 63475662387234505765",
        "to": "Счет 8175128657841941437",
    },
    {
        "id": 129309161,
        "date": "2018-09-26T00:46:36.256087",
        "operationAmount": {"amount": "17250", "currency": {"code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from": "Visa Classic 1313132313442324",
        "to": "Счет 1743370781324891402",
    },
    {
        "id": 999888555,
        "date": "2025-03-19T10:3:58.027767",
        "operationAmount": {"amount": "250", "currency": {"code": "RUB"}},
        "description": "Перевод организации STMU",
        "from": "Счет - 63475662387234505765",
        "to": "Счет 8175128657841941437",
    },
]
usd_transactions_list = list(filter_by_currency(transactions, "RUB"))
number_of_iterations = len(usd_transactions_list)
for i in range(number_of_iterations):
    print(usd_transactions_list[i])


def transaction_descriptions(transaction: list[dict[str, int | str]]) -> Generator[int | str, Any, None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for num in transaction:
        yield num["description"]


descriptions = transaction_descriptions(usd_transactions_list)
for i in range(number_of_iterations):
    print(next(descriptions))
