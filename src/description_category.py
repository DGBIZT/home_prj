import re
from collections import Counter

def list_dict_operation(list_dict: list[dict[str, str]], search_string: str) -> list[dict[str, str]]:

    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
        а возвращает список словарей, у которых в описании есть данная строка."""

    pattern = re.compile(search_string)
    new_list_dict = list()
    for item in list_dict:
        b= item.get("state")
        if b and pattern.match(b):
            new_list_dict.append(item)
    return new_list_dict


# list_sort_data =  [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     ]
#
# print(list_dict_operation(list_sort_data, "EXECUTED"))


def count_operations_by_category(operations: list[dict[str, str]], categories: list) -> dict:

    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    # all_categories = [operation.get("description") for operation in operations]

    all_categories = list()

    for operation in operations:
        transaction_category = operation.get("description")
        all_categories.append(transaction_category)

    category_count = Counter(all_categories)

    # filtered_category_count = {category: category_count[category] for category in categories}
    filtered_category_count = {}
    for category in categories:
        if category in category_count:
            filtered_category_count[category] = category_count[category]

    return filtered_category_count

# operations = [
#     {"id": 1, "amount": 100.0, "description": "groceries"},
#     {"id": 2, "amount": 200.0, "description": "utilities"},
#     {"id": 3, "amount": 50.0, "description": "groceries"},
#     {"id": 4, "amount": 150.0, "description": "entertainment"},
# ]
#
# categories = ["groceries", "utilities", "entertainment", "transport"]
#
# print(count_operations_by_category(operations, categories))