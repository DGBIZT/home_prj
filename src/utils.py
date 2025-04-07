import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8", delay=False)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s)")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_for_city(file_path: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, file_path)
    try:
        logger.info(f"Записываем данные в файл {file_path}")
        with open(full_path, "r", encoding="UTF-8") as f:
            try:
                data = json.load(f)
                if type(data) is not list:
                    return []
                return data
            # Ошибка обработки, декодирования файла
            except json.JSONDecodeError as ex:
                logger.error(f"Ошибка обработки, декодирования файла: {ex}")
                return list()
            # Файл не найден
    except FileNotFoundError as ex:
        logger.error(f"Файл не найден: {ex}")
        return list()


# a = get_for_city("../data/operations.json")
# print(a)
