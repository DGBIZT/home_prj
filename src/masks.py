def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""

    if len(card_number) == 16:
        mask_card_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""

    if len(account_number) == 20:
        mask_account_number = f"**{account_number[-4:]}"

    return mask_account_number
