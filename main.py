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
