from src.utils import get_for_city
from src.description_category import list_dict_operation
from src.processing import sort_by_date
from src.widget import get_date, mask_account_card
from src.file_operations import read_transactions_csv_and_output, read_transactions_excel_and_output


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

      while True:
            third_question = input().strip().lower()
            if third_question not in {yes, no}:
                  print (f"Введите {yes} или {no}")
                  continue

            if third_question == yes:
                  new_ruble_list = list()
                  for item in sorted_in_ascending_order:
                        if "operationAmount" in item:
                              has_rub = any(item["operationAmount"]["currency"]["code"] == 'RUB' for item in sorted_in_ascending_order)
                              if not has_rub:
                                    print("По данной транзакции данных нет, выберите другой вариант")
                                    continue
                              currency = item["operationAmount"]["currency"]["code"]
                              if currency == 'RUB':
                                    new_ruble_list.append(item)
                                    break

                        if not "operationAmount" in item:
                              # проверка есть ли "RUB" TRU или FALSE
                              has_rub = any(item['currency_code'] == 'RUB' for item in sorted_in_ascending_order)
                              if not has_rub:
                                    print("По данной транзакции данных нет, выберите другой вариант")
                                    continue
                              if has_rub:
                                    currency = item['currency_code']
                                    if currency == 'RUB':
                                          new_ruble_list.append(item)
                                          break
                  break

            if third_question == no:
                  new_ruble_list = sorted_in_ascending_order
                  break


      print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
      fourth_question = input().strip().lower()
      if fourth_question == "да":
            print("Введите 'Перевод' или 'Открытие'.")
            open_word = "открытие"
            transaction_word = 'перевод'
            while True:
                  fourth_question_yes = input().strip().lower()
                  if fourth_question_yes not in {open_word, transaction_word}:
                        print("Введите 'Перевод' или 'Открытие'.")
                        continue
                  certain_word_list_of_dicts = list_dict_operation(new_ruble_list, fourth_question_yes)

                  if not certain_word_list_of_dicts:
                        print(f"Транзакции по слову {fourth_question_yes} нет")
                  else:
                        certain_word_list_of_dicts = certain_word_list_of_dicts
                        # print(certain_word_list_of_dicts)
                        break
      elif fourth_question == "нет":
            certain_word_list_of_dicts = new_ruble_list

      # Создаю список из значений словаря
      categories_list = list()
      for item in certain_word_list_of_dicts:
            if item["description"]:
                  categories_list.append(item["description"])
      # print(categories_list)

      print("Распечатываю итоговый список транзакций...")
      print(f"Всего банковских операций в выборке: {len(categories_list)}")

      for operation in certain_word_list_of_dicts:

            if not "operationAmount" in operation:
                  date = get_date(operation["date"])
                  transactions = operation["description"]
                  transfer_from = operation.get("from")
                  if transfer_from and isinstance(transfer_from, str):
                        transfer_from = mask_account_card(transfer_from)
                  else:
                        transfer_from = None
                  # transfer_from = mask_account_card(operation.get("from", 'default_value'))
                  transfer_to = mask_account_card(operation["to"])
                  transfer_amount = operation["amount"]
                  currency_name = operation['currency_code']

                  print("\n"f"{date} {transactions}")
                  if not transfer_from:
                        print(f'{transfer_to}')
                  else:
                        print(f"{transfer_from} -> {transfer_to}")
                  print(f"Сумма: {transfer_amount} {currency_name}")

            if "operationAmount" in operation:
                  date = get_date(operation["date"])
                  transactions = operation["description"]
                  transfer_from = operation.get("from")
                  if transfer_from and isinstance(transfer_from, str):
                        transfer_from = mask_account_card(transfer_from)
                  else:
                        transfer_from = None
                  # transfer_from = mask_account_card(operation["from"])
                  transfer_to = mask_account_card(operation["to"])
                  transfer_amount = operation["operationAmount"]["amount"]
                  currency_name = operation["operationAmount"]["currency"]["name"]
                  # f"\n"f"{date} {transactions}\n{transfer_from} -> {transfer_to}\nСумма: {transfer_amount} {currency_name}"

                  print("\n"f"{date} {transactions}")
                  if not transfer_from :
                        print(f'{transfer_to}')
                  else:
                        print(f"{transfer_from} -> {transfer_to}")
                  print(f"Сумма: {transfer_amount} {currency_name}")


choose_difficulty()
