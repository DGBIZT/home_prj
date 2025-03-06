def filter_by_state(list_of_dicts: list[dict[str, int | str]], state: str = "EXECUTED") -> list:

    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 'state'
    соответствует указаному значению"""

    new_list = []
    for item in list_of_dicts:
        if item["state"] == state:
            new_list.append(item)
    return new_list


new_list_of_dicts = filter_by_state(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)
print(new_list_of_dicts)


def sort_by_date(list_of_dicts: list[dict[str, int | str]]) -> list:

    """Функция, которая принимает список словарей и возвращает новый список, отсортированный по дате"""

    new_list_sort_data = sorted(list_of_dicts, key=lambda new_list: new_list["date"], reverse=True)
    return new_list_sort_data


list_sort_data = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
)
print(list_sort_data)
