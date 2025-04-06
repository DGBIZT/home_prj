
from src.utils import get_for_city
from unittest.mock import patch
import tempfile




@patch('src.utils.get_for_city')  # Убедись, что путь указан правильно
def test_get_for_city(mock_get_for_city):
    expected_data = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]
    mock_get_for_city.return_value = expected_data
    # result = get_for_city("../data/operations.json")
    # print(f"Результат вызова get_for_city: {result}")
    assert mock_get_for_city("../data/operations.json") == expected_data
    mock_get_for_city.assert_called_once_with("../data/operations.json")


def test_get_for_city_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = get_for_city('non_existent_file.txt')
        assert result == []

def test_get_for_city_with_invalid_data():
    invalid_json_data = "{invalid_json}"
    result = get_for_city(invalid_json_data)
    assert result == []


def test_get_for_city_type_not_list():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'{"key": "value"}')
        result = get_for_city(temp_file.name)
        assert result == []


def test_get_for_city_type_list():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'[1, 2, 3]')
        temp_file.seek(0)
        result = get_for_city(temp_file.name)
        assert result == [1, 2, 3]