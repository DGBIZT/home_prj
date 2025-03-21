# Привет, меня зовут Георгий. Я начинающий Python-разработчик
### Проект New Widget

1. Описание:
```
В этом проекте для крупного банка создаю новую фичу для личного кабинета клиента.Это виджет, который показывает несколько последних успешных банковских операций клиента.
```
2. Клонируйте репозиторий:
```
git clone https://github.com/DGBIZT/home_prj.git
```
3. Установка:
```
poetry install
```

4. Обновите зависимостей
```
poetry update
```
5. Тестирование
```
htmlcov/index.html
```
6. Модуль Generators
```
Модуль generators предоставляет функции для работы с массивами транзакций. Он включает в себя следующие функции:

- filter_by_currency(transaction, forex:): фильтрует транзакции по заданной валюте и возвращает итератор.
- transaction_descriptions(transaction): генератор, возвращающий описания транзакций.
- card_number_generator(start, end): генератор, который выводит номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ.

### Примеры использования:

```python
# Пример использования filter_by_currency
usd_transactions_list = list(filter_by_currency(transactions, "USD"))
number_of_iterations = len(usd_transactions_list)
for i in range(number_of_iterations):
    print(usd_transactions_list[i])

# Пример использования transaction_descriptions
descriptions = transaction_descriptions(usd_transactions_list)
for i in range(number_of_iterations):
    print(next(descriptions))

# Пример использования card_number_generator
for card in card_number_generator(4000123456789010, 4000123456789015):
    print(card)
```
### Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).


