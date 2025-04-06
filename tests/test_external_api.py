import os
from unittest.mock import patch

import requests
from dotenv import load_dotenv

from src.external_api import transaction_amount


@patch("src.external_api.transaction_amount")
def test_transaction_amount(mock_transaction_amount):
    expected_data = 31957.58
    mock_transaction_amount.return_value = expected_data

    assert (
        mock_transaction_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == expected_data
    )
    mock_transaction_amount.assert_called_once_with(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )


def test_load_dotenv():
    with patch.dict("os.environ", {"API_KEY": "test_key"}):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        assert api_key == "test_key"


def test_transaction_amount_request_exception():
    with patch("requests.request", side_effect=requests.exceptions.RequestException):
        result = transaction_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        assert result == 0
