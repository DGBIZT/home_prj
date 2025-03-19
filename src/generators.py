from typing import Iterator
from operator import itemgetter

def filter_by_currency(transaction: list[dict[str, int | str]], forex: str) -> Iterator[dict[str, int | str]]:
     currency_code = list((x for x in transaction if x["operationAmount"]["currency"]["code"] == forex))
     yield currency_code


transactions = [
    {
        "id": 970157810,
        "date": "2018-06-08T10:3:58.027767",
        "operationAmount": {"amount": "150", "currency": {"code": "USD"}},
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
        "operationAmount": {"amount": "250", "currency": {"code": "USD"}},
        "description": "Перевод организации STMU",
        "from": "Счет - 63475662387234505765",
        "to": "Счет 8175128657841941437",
    },
]
usd_transactions = filter_by_currency(transactions, "RUB")
for _ in range(1):
    print(*(next(usd_transactions)))
