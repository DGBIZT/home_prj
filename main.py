from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# Маскировка номера банковской карты
print(get_mask_card_number("7000792289606361"), "\n")

# Маскировка номера банковского счета
print(get_mask_account("73654108430135874305"), "\n")

# Обработка информации как о картах, так и о счетах
print(mask_account_card("Visa Electron 1234567890123456"), "\n")

# Обработка даты
print(get_date("2024-03-11T02:26:18.671407"), "\n")

# Возвращает новый список словарей у которых ключ 'state' соответствует указанному значению
new_list_of_dicts = filter_by_state(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)
print(new_list_of_dicts, "\n")

# Возвращает новый список, отсортированный по дате
list_sort_data = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
)
print(list_sort_data, "\n")

""" GENERATORS"""
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
usd_transactions_list = list(filter_by_currency(transactions, "USD"))
number_of_iterations = len(usd_transactions_list)
for i in range(number_of_iterations):
    print(usd_transactions_list[i])

descriptions = transaction_descriptions(usd_transactions_list)
for i in range(number_of_iterations):
    print(next(descriptions))

for card_number in card_number_generator(4000123456789010, 4000123456789015):
    print(card_number)
