from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    split_card = card.split(" ")
    if len(split_card[-1]) == 16:
        mask_ac_card = f"{" ".join(split_card[:-1])} {get_mask_card_number(split_card[-1])}"
    else:
        mask_ac_card = f"{" ".join(split_card[:-1])} {get_mask_account(split_card[-1])}"

    return mask_ac_card
