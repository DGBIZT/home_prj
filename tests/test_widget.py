import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card_visa(mask_account_card_visa):
    assert mask_account_card("Visa Electron 1234567890123456") == mask_account_card_visa

def test_mask_account_card_maestro(mask_account_card_maestro):
    assert mask_account_card("Maestro 7000792289606361") == mask_account_card_maestro

def test_mask_account_card_score(mask_account_card_score):
    assert mask_account_card("Счет 73654108430135874305") == mask_account_card_score

def test_mask_account_card_mastercard(mask_account_card_mastercard):
    assert mask_account_card("MasterCard 7158300734726758") == mask_account_card_mastercard

    with pytest.raises(AttributeError):
        mask_account_card(125)
    with pytest.raises(AttributeError):
        mask_account_card(None)


def test_get_date(date):
    assert get_date("2024-03-11T02:26:18.671407") == date


    with pytest.raises(UnboundLocalError):
        get_date("11-03-2020T02:26:18.671407")
    with pytest.raises(UnboundLocalError):
        get_date("024-03-11T02:26:18.671407")
    with pytest.raises(UnboundLocalError):
        get_date("")