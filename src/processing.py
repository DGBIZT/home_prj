from src.widget import get_date
def filter_by_state(list_of_dicts: list[dict[str, int | str]], state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 'state'
    соответствует указаному значению"""

    new_list = []
    for item in list_of_dicts:
        if item["state"] == state:
            new_list.append(item)
    if new_list == []:
            raise NameError("Заданный ключ state отсутствует")

    return new_list

def sort_by_date(list_of_dicts: list[dict[str, int | str]], state: bool = None) -> list:
    """Функция, которая принимает список словарей и возвращает новый список, отсортированный по дате"""

    for item in list_of_dicts:
       if get_date(item["date"]):
           if state is None:
               list_of_dicts = sorted(list_of_dicts, key=lambda new_list: new_list["date"], reverse=True)
           else:
               list_of_dicts = sorted(list_of_dicts, key=lambda new_list: new_list["date"])

    return list_of_dicts