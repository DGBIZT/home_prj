# from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
# from src.masks import get_mask_account, get_mask_card_number
# from src.processing import filter_by_state, sort_by_date
# from src.widget import get_date, mask_account_card
# from src.file_operations import read_transactions_csv_and_output, read_transactions_excel_and_output

# # Маскировка номера банковской карты
# print(get_mask_card_number("7000792289606361"), "\n")
#
# # Маскировка номера банковского счета
# print(get_mask_account("73654108430135874301"), "\n")
#
# # Обработка информации как о картах, так и о счетах
# print(mask_account_card("Visa Electron 1234567890123456"), "\n")
#
# # Обработка даты
# print(get_date("2024-03-11T02:26:18.671407"), "\n")
#
# # Возвращает новый список словарей у которых ключ 'state' соответствует указанному значению
# new_list_of_dicts = filter_by_state(
#     [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
# )
# print(new_list_of_dicts, "\n")
#
# # Возвращает новый список, отсортированный по дате
# list_sort_data = sort_by_date(
#     [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     ]
# )
# print(list_sort_data, "\n")
#
# """ GENERATORS"""
# transactions = [
#     {
#         "id": 970157810,
#         "date": "2018-06-08T10:3:58.027767",
#         "operationAmount": {"amount": "150", "currency": {"code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Счет - 63475662387234505765",
#         "to": "Счет 8175128657841941437",
#     },
#     {
#         "id": 129309161,
#         "date": "2018-09-26T00:46:36.256087",
#         "operationAmount": {"amount": "17250", "currency": {"code": "USD"}},
#         "description": "Перевод с карты на счет",
#         "from": "Visa Classic 1313132313442324",
#         "to": "Счет 1743370781324891402",
#     },
#     {
#         "id": 999888555,
#         "date": "2025-03-19T10:3:58.027767",
#         "operationAmount": {"amount": "250", "currency": {"code": "USD"}},
#         "description": "Перевод организации STMU",
#         "from": "Счет - 63475662387234505765",
#         "to": "Счет 8175128657841941437",
#     },
# ]
# usd_transactions_list = list(filter_by_currency(transactions, "USD"))
# number_of_iterations = len(usd_transactions_list)
# for i in range(number_of_iterations):
#     print(usd_transactions_list[i])
#
# descriptions = transaction_descriptions(usd_transactions_list)
# for i in range(number_of_iterations):
#     print(next(descriptions))
#
# for card_number in card_number_generator(4000123456789010, 4000123456789015):
#     print(card_number)
#
# csv_file = read_transactions_csv_and_output("../data/transactions.csv")
# print(csv_file)
#
# xlsx_file = read_transactions_excel_and_output("../data/transactions_excel.xlsx")
# print(xlsx_file)
####################################################
from src.utils import get_for_city
from src.description_category import list_dict_operation
from src.processing import sort_by_date
from src.widget import get_date, mask_account_card
from src.file_operations import read_transactions_csv_and_output, read_transactions_excel_and_output
import re

from tests.conftest import transaction


def choose_difficulty():
      """Запрашивает у пользователя пункт меню. """
      one = "1"
      two = "2"
      three = "3"
      print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
      print(f'Выберите необходимый пункт меню:\n'
      f'{one}. Получить информацию о транзакциях из JSON-файла\n'
      f'{two}. Получить информацию о транзакциях из CSV-файла\n'
      f'{three}. Получить информацию о транзакциях из XLSX-файла')


      while True:
            options = input().strip()
            if options in {one, two, three}:
                  break
            print("Пожалуйста введите 1, 2 или 3")

      if options == one:
            conclusion = "Для обработки выбран JSON-файл"
            transaction_file = get_for_city("../data/operations.json")

      elif options == two:
            conclusion = "Для обработки выбран CSV-файл"
            transaction_file = read_transactions_csv_and_output("../data/transactions.csv")
      elif options == three:
            conclusion = "Для обработки выбран XLSX-файл"
            transaction_file = read_transactions_excel_and_output("../data/transactions_excel.xlsx")

      # print(conclusion)
      print(conclusion)



      """Функция запрашивает статус у пользователя по которому необходимо выполнить фильтрацию"""
      executed = "EXECUTED"
      canceled = "CANCELED"
      pending = "PENDING"

      print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
      "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

      while True:
            status_operation = input().strip().upper()

            if status_operation not in {executed, canceled, pending}:
                print(f"Статус {status_operation} не доступен")
                continue

            new_list_of_dicts = list_dict_operation(transaction_file, status_operation)

            if not new_list_of_dicts:
                  print(f"Статус {status_operation} не доступен")
            else:
                new_list_of_dicts = new_list_of_dicts
                break
      # print(new_list_of_dicts)

      print(f"Операции отфильтрованы по статусу {status_operation.upper()}")

      # print(new_list_of_dicts)

      print("Отсортировать операции по дате? Да/Нет")

      yes = "да"
      no = "нет"
      while True:
            first_question = input().strip().lower()
            if first_question not in {yes, no}:
                  print (f"Введите {yes} или {no}")
                  continue

            if first_question == yes:
                  sort_date = sort_by_date(new_list_of_dicts)
                  # print(sort_date)
                  break
            if first_question == no:
                  sort_date = new_list_of_dicts
                  # print(sort_date)
                  break

      print("Отсортировать по возрастанию или по убыванию?")
      second_question = input().strip().lower()
      if second_question == "возрастанию":
            sorted_in_ascending_order = sorted(sort_date, key=lambda date_sort: date_sort["date"])
            # print(sorted_in_ascending_order)
      elif second_question == "убыванию":
            sorted_in_ascending_order = sorted(sort_date, key=lambda date_sort: date_sort["date"], reverse=True)
            # print(sorted_in_ascending_order)

      print("Выводить только рублевые транзакции? Да/Нет")
      #
      # third_question = input().strip().lower()
      # if third_question == 'да':
      #       new_ruble_list = list()
      #       for item in sorted_in_ascending_order:
      #             currency = item["operationAmount"]["currency"]["code"]
      #             if currency == "RUB":
      #                   new_ruble_list.append(item)
      #       # print(new_ruble_list)
      #
      # print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
      # fourth_question = input().strip().lower()
      # if fourth_question == "да":
      #       print("Введите 'Перевод' или 'Открытие'.")
      #       open_word = "открытие"
      #       transaction_word = 'перевод'
      #       while True:
      #             fourth_question_yes = input().strip().lower()
      #             if fourth_question_yes not in {open_word, transaction_word}:
      #                   print("Введите 'Перевод' или 'Открытие'.")
      #                   continue
      #             certain_word_list_of_dicts = list_dict_operation(new_ruble_list, fourth_question_yes)
      #
      #             if not certain_word_list_of_dicts:
      #                   print(f"Транзакции по слову {fourth_question_yes} нет")
      #             else:
      #                   certain_word_list_of_dicts = certain_word_list_of_dicts
      #                   break
      # # Создаю список из значений словаря
      # categories_list = list()
      # for item in certain_word_list_of_dicts:
      #       if item["description"]:
      #             categories_list.append(item["description"])
      #
      #
      # print("Распечатываю итоговый список транзакций...")
      # print(f"Всего банковских операций в выборке: {len(categories_list)}")
      #
      # for operation in certain_word_list_of_dicts:
      #       date = get_date(operation["date"])
      #       transactions = operation["description"]
      #       transfer_from =mask_account_card(operation["from"])
      #       transfer_to = mask_account_card(operation["to"])
      #       transfer_amount = operation["operationAmount"]["amount"]
      #       currency_name = operation["operationAmount"]["currency"]["name"]
      #       #f"\n"f"{date} {transactions}\n{transfer_from} -> {transfer_to}\nСумма: {transfer_amount} {currency_name}"
      #       print("\n"f"{date} {transactions}")
      #       print(f"{transfer_from} -> {transfer_to}")
      #       print(f"Сумма: {transfer_amount} {currency_name}")
      #




choose_difficulty()
