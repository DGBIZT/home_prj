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
        headers = {"apikey": api_key}
        try:
            response = requests.request("GET", url, headers=headers, data=payload)

        except requests.exceptions.RequestException:
            print("ошибка http запроса")
            return 0
        else:
            result = response.text
            json_data = json.loads(result)
            return round(json_data["result"], 2)
            # return json_data

print(transaction_amount({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}))