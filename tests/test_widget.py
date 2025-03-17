import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Electron 1234567890123456", "Visa Electron 1234 56** **** 3456"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

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
