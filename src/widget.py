from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах"""

    if card == int or card is None:
        raise AttributeError("Введите строковое значение")
    else:
        split_card = card.split(" ")
        if len(split_card[-1]) == 16:
            mask_ac_card = f"{" ".join(split_card[:-1])} {get_mask_card_number(split_card[-1])}"
        else:
            mask_ac_card = f"{" ".join(split_card[:-1])} {get_mask_account(split_card[-1])}"

    return mask_ac_card


def get_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """

    if date == int or date is None:
        raise AttributeError("Введите значение с датой")
    else:
        split_date = date.split("-")
        if len(split_date[0]) != 4:
            raise UnboundLocalError("Введите значение с датой в формате 2024-03-11T02:26:18.671407")
        else:
            data_new = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return data_new
