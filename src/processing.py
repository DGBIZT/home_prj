def filter_by_state(list_of_dicts: list[dict[str, int | str]], state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 'state'
    соответствует указаному значению"""

    new_list = []
    for item in list_of_dicts:
        if item["state"] == state:
            new_list.append(item)

    return new_list


def sort_by_date(list_of_dicts: list[dict[str, int | str]]) -> list:
    """Функция, которая принимает список словарей и возвращает новый список, отсортированный по дате"""

    new_list_sort_data = sorted(list_of_dicts, key=lambda new_list: new_list["date"], reverse=True)

    return new_list_sort_data
