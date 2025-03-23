import pytest


@pytest.fixture
def mask_card_number():
    return "7000 79** **** 6361"


@pytest.fixture
def mask_account():
    return "**4305"


@pytest.fixture
def date():
    return "11.03.2024"


@pytest.fixture
def sort_by_date_False():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_same():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def sort_by_date_True():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def transaction_descriptions_mylist():
    return [
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
@pytest.fixture
def transaction():
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
            "operationAmount": {"amount": "250", "currency": {"code": "RUB"}},
            "description": "Перевод организации STMU",
            "from": "Счет - 63475662387234505765",
            "to": "Счет 8175128657841941437",
        },
    ]
    return transactions
@pytest.fixture
def transaction_rub():
    return [{
            "id": 999888555,
            "date": "2025-03-19T10:3:58.027767",
            "operationAmount": {"amount": "250", "currency": {"code": "RUB"}},
            "description": "Перевод организации STMU",
            "from": "Счет - 63475662387234505765",
            "to": "Счет 8175128657841941437",
        }]
