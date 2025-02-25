from .masks import get_mask_account, get_mask_card_number


"""Функция которая обрабатывает информацию как о картах, так и о счетах"""


def mask_account_card(card: str) -> str:
    split_card = card.split(" ")
    if len(split_card[-1]) == 16:
        mask_ac_card = f"{" ".join(split_card[:-1])} {get_mask_card_number(split_card[-1])}"
    else:
        mask_ac_card = f"{" ".join(split_card[:-1])} {get_mask_account(split_card[-1])}"

    return mask_ac_card


"""Функция которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
 и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """


def get_date(date: str) -> str:
    data_new = f"{date[8:10]}.{date[5:7]}.{date[:4]}"

    return data_new
