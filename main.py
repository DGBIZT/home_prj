from src.masks import get_mask_account, get_mask_card_number

# Маскировка номера банковской карты
print(get_mask_card_number("7000792289606361"))

# Маскировка номера банковского счета
print(get_mask_account("73654108430135874305"))
