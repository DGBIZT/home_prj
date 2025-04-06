import json
import os


def get_for_city(file_path: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, file_path)
    try:
        with open(full_path, "r", encoding="UTF-8") as f:
            try:
                data = json.load(f)
                if type(data) is not list:
                    return []
                return data
            # Ошибка обработки, декодирования файла
            except json.JSONDecodeError:
                return list()
            # Файл не найден
    except FileNotFoundError:
        return list()
