from typing import Any, Generator, Iterator


def filter_by_currency(transaction: list[dict[str, int | str]], forex: str) -> Iterator[list[dict[str, int | str]]]:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции"""

    if transaction == []:
        raise TypeError("Ваш список пуст, заполните его")
    elif forex == "":
        raise TypeError("Введите валюту для получения информации")

    for _ in range(len(transaction)):
        total_number = 0
        for item in transaction:
            if item["operationAmount"]["currency"]["code"] != forex:
                total_number += 1
    if total_number == len(transaction):
        raise TypeError("По данной валюте нет транзакций!")
    else:
        currency_code = list((x for x in transaction if x["operationAmount"]["currency"]["code"] == forex))
        for item in currency_code:
            yield item


def transaction_descriptions(transaction: list[dict[str, int | str]]) -> Generator[int | str, Any, None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for num in transaction:
        yield num["description"]


def card_number_generator(start: int, stop: int) -> Generator[int | str, Any, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X - цифра номера карты"""

    for num in range(start, stop + 1):
        str_num = str(num)
        str_num = "000000000000000" + str_num
        # print(str_num)
        yield f"{str_num[-16:-12]} {str_num[-12:-8]} {str_num[-8:-4]} {str_num[-4:]}"


