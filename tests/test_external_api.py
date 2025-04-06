from unittest.mock import patch

import pytest
from dotenv import load_dotenv
import os
import requests

from src.external_api import transaction_amount


@patch('src.external_api.transaction_amount')
def test_transaction_amount(mock_transaction_amount):
    expected_data = 31957.58
    mock_transaction_amount.return_value = expected_data
    # result = transaction_amount({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'})
    # print(f"Результат вызова transaction_amount: {result}")
    assert mock_transaction_amount({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'})== expected_data
    mock_transaction_amount.assert_called_once_with({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'})

# @patch("requests.get")
# def test_transaction_amount_requests(mock_get):
#     mock_get.return_value.json.return_value = 697457.16
#     assert transaction_amount({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}) == 697457.16
#     mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert")

# 'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1743931443, 'rate': 84.834664}, 'date': '2025-04-06', 'result': 697457.16157

def test_load_dotenv():
    with patch.dict('os.environ', {'API_KEY': 'test_key'}):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        assert api_key == 'test_key'

def test_transaction_amount_request_exception():
    with patch('requests.request', side_effect=requests.exceptions.RequestException):
        result = transaction_amount({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'})
        assert result == 0





