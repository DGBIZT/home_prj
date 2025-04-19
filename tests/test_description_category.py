import pytest
from src.description_category import list_dict_operation, count_operations_by_category

list_sort_data =  [
        {"id": 41428829, "state": "EXECUTED ", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

def test_list_dict_operation():
    assert list_dict_operation(list_sort_data, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED ", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_list_dict_operation_empty_list():
    with pytest.raises(ValueError) as exc_info:
        list_dict_operation([], "test")
    assert str(exc_info.value) == "Список операций пуст"

def test_list_dict_operation_empty_search_string():
    with pytest.raises(ValueError) as exc_info:
        list_dict_operation(list_sort_data, " ")  # Передаём строку из пробелов

    assert str(exc_info.value) == "Строка поиска не может быть пустой"

def test_list_dict_operation_invalid_regex():
    # Передаём некорректный regex-шаблон (например, "[" без закрывающей скобки)
    with pytest.raises(ValueError) as exc_info:
        list_dict_operation(list_sort_data, "[")

    # Проверяем, что сообщение об ошибке содержит нужный текст
    assert "Некорректный шаблон поиска" in str(exc_info.value)


operations = [
    {"id": 1, "amount": 100.0, "description": "groceries"},
    {"id": 2, "amount": 200.0, "description": "utilities"},
    {"id": 3, "amount": 50.0, "description": "groceries"},
    {"id": 4, "amount": 150.0, "description": "entertainment"},
]

categories = ["groceries", "utilities", "entertainment", "transport"]

def test_count_operations_by_category():
    assert count_operations_by_category(operations, categories) == {'groceries': 2, 'utilities': 1, 'entertainment': 1}



