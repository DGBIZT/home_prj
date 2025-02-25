from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

# Маскировка номера банковской карты
print(get_mask_card_number("7000792289606361"))

# Маскировка номера банковского счета
print(get_mask_account("73654108430135874305"))

# Обрабатка информации как о картах, так и о счетах
print(mask_account_card("Счет 73654108430135874305"))

# Обработка даты
print(get_date("2024-03-11T02:26:18.671407"))
