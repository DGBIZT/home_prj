import csv
import os

import pandas as pd


def read_transactions_csv_and_output(file_path: str) -> list[dict[str, str]]:
    """Функция для считывания финансовых операций из CSV"""

    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, file_path)

    with open(full_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        reader = pd.DataFrame(list(reader))
        reader.columns = reader.iloc[0]  # Установи первую строку как заголовки столбцов
        reader = reader.drop(0)  # Удали первую строку, так как она теперь заголовок
        list_of_dicts = reader.to_dict(orient="records")
        return list_of_dicts


def read_transactions_excel_and_output(file_path: str) -> list[dict[str, str]]:
    """Функция для считывания финансовых операций из Excel"""

    bas_dir = os.path.dirname(__file__)
    full_path = os.path.join(bas_dir, file_path)

    excel_data = pd.read_excel(full_path)
    list_of_dicts = excel_data.to_dict(orient="records")
    return list_of_dicts
