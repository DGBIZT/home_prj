import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8", delay=False)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s)")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info(f"Обрабатываем номер карты {card_number}")
    if len(card_number) == 16:
        mask_card_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return mask_card_number
    else:
        logger.error("Номер карты должен содержать 16 цифр")
        raise ValueError("Номер карты должен содержать 16 цифр")


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""

    logger.info(f"Обрабатываем номер банковского счета {account_number}")
    if len(account_number) == 20:
        mask_account_number = f"**{account_number[-4:]}"
        return mask_account_number
    else:
        logger.error("Номер банковского счета должен содержать 20 цифр")
        raise ValueError("Номер банковского счета должен содержать 20 цифр")
