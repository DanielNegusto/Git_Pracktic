# Проект по обработке данных

## Описание проекта

Этот проект предназначен для обработки и маскирования номеров карт и счётов, а также для фильтрации и сортировки списка операций по дате и статусу.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-repo/project-name.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd project-name
    ```

3. Установите необходимые зависимости:
    ```bash
    # для первичной установки
     poetry install
    # для обновления
    poetry update
    ```

## Использование

### Маскирование карт и счётов


### Функции фильтрации транзакций по валюте

#### Filter_by_currency

Фильтрует транзакции по заданной валюте.
### Функции генерации описаний транзакций

#### transaction_descriptions

Генерирует описания транзакций по очереди.
### Генератор номеров банковских карт

#### card_number_generator

Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
# Тестирование
Для тестирования используйте библиотеку pytest. В проекте включены тесты для всех основных функций.

# Запуск тестов
Убедитесь, что у вас установлен pytest

Запустите тесты из корневой директории проекта:
```bash
pytest
```
### Проект покрыт тестами с использованием pytest. Для запуска тестов выполните команду:

```bash
pytest --cov=src tests/
```
# Тестируемые функции
## Модуль mask.py
### Get_mask_card_number:

* Тестирование правильности маскирования номера карты.
* Проверка работы функции на различных входных форматах номеров карт.
* Проверка корректности обработки отсутствующих номеров карт.

### get_mask_account:

* Тестирование правильности маскирования номера счёта.
* Проверка работы функции с различными форматами и длинами номеров счётов.
* Проверка корректности обработки коротких номеров счётов.

## Модуль processing.py
### filter_by_state:

* Тестирование фильтрации списка словарей по заданному статусу state.
* Проверка работы функции при отсутствии словарей с указанным статусом.

### sort_by_date:

* Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
* Проверка корректности сортировки при одинаковых датах.
* Тесты на работу функции с некорректными или нестандартными форматами дат.

## Модуль generators.py

### filter_by_currency:

* Тестирование фильтрации транзакций по заданной валюте.
* Проверка корректности фильтрации, когда транзакции с заданной валютой присутствуют в списке.
* Убедитесь, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
* Тестирование работы функции с различными валютами, включая стандартные и нестандартные валютные коды.
* Проверка, что функция не вызывает ошибок при обработке пустого списка или без соответствующих валютных операций.

### transaction_descriptions:

* Тестирование корректности генерации описаний транзакций.
* Проверьте, что функция возвращает ожидаемые описания для каждой транзакции в списке.
* Тестируйте работу функции с различным количеством входных транзакций, включая пустой список.
* Убедитесь, что функция корректно обрабатывает случаи отсутствия описаний в транзакциях.

### card_number_generator:

* Тестирование генерации номеров банковских карт в заданном диапазоне.
* Проверка корректности форматирования сгенерированных номеров карт.
* Убедитесь, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.

## Модуль decorators

### log

Декоратор `log` используется для автоматического логирования начала и конца выполнения функции, а также ее результатов или возникших ошибок.

### При успешном выполнении функции, в файл mylog.txt будет записано:
```
"function_name" ok
```
### При возникновении ошибки:
```
"function_name" error:  Inputs: (a, b), {}
```
### Если filename не указан, логи будут выводиться в консоль.