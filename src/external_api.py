import json
import os

import requests
from dotenv import load_dotenv


def transaction_amount(transaction_dict: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    amount = transaction_dict["operationAmount"]["amount"]
    currency = transaction_dict["operationAmount"]["currency"]["code"]
    to_forex = "RUB"

    if currency == "RUB":

        return round(float(amount), 2)

    else:
        load_dotenv()
        api_key = os.getenv("API_KEY")

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_forex}&from={currency}&amount={amount}"
        payload = {}
        headers = {"apikey": f"{api_key}"}
        try:
            response = requests.request("GET", url, headers=headers, data=payload)

        except requests.exceptions.RequestException:
            print("ошибка http запроса")
            return 0
        else:
            result = response.text
            json_data = json.loads(result)
            return round(json_data["result"], 2)
