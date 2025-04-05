import json


def get_for_city(file_path: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                return list()
    except FileNotFoundError:
        return list()


a = get_for_city("data/operations.json")
print(a)