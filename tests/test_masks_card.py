import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

    with pytest.raises(ValueError):
        get_mask_card_number("123456789101112131415")

    with pytest.raises(ValueError):
        get_mask_card_number(" ")

def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"

    with pytest.raises(ValueError):
        get_mask_account("123456")

    with pytest.raises(ValueError):
        get_mask_account(" ")


def test_mask_account_card():
    assert mask_account_card("Visa Electron 1234567890123456") == "Visa Electron 1234 56** **** 3456"
    assert mask_account_card("Maestro 7000792289606361") == "Maestro 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    with pytest.raises(AttributeError):
        mask_account_card(125)
    with pytest.raises(AttributeError):
        mask_account_card(None)

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    with pytest.raises(UnboundLocalError):
        get_date("11-03-2020T02:26:18.671407")
    with pytest.raises(UnboundLocalError):
        get_date("024-03-11T02:26:18.671407")




