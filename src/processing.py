from src.widget import get_date


def filter_by_state(list_of_dicts: list[dict[str, int | str]], state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 'state'
    соответствует указанному значению"""

    new_list = []
    for item in list_of_dicts:
        if item["state"] == state:
            new_list.append(item)
    if new_list == list():
        raise NameError("Заданный ключ state отсутствует")

    return new_list


def sort_by_date(list_of_dicts: list[dict[str, int | str]], state: bool = False) -> list:
    """Функция, которая принимает список словарей и возвращает новый список, отсортированный по дате"""
    if list_of_dicts == []:
        raise UnboundLocalError("Ваш список пуст, заполните список что бы провести сортировку")
    for item in list_of_dicts:
        if isinstance(item["date"], str):
            if get_date(item["date"]):
                split_date = item["date"].split("-")
                if len(split_date[0]) != 4:
                    raise UnboundLocalError("Введите значение с датой в формате 2024-03-11T02:26:18.671407")
                if state is False:
                    list_of_dicts = sorted(list_of_dicts, key=lambda new_list: new_list["date"], reverse=True)
                else:
                    list_of_dicts = sorted(list_of_dicts, key=lambda new_list: new_list["date"])
        else:
            raise SyntaxError("Дата должна быть строковым типом данных")

    return list_of_dicts
