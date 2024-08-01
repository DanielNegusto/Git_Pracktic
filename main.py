from typing import List, Optional

from src.generators import filter_by_currency
from src.logging_config import logger
from src.processing import filter_by_state, filter_rub_transactions, filter_transactions_by_description, sort_by_date
from src.utils import read_transactions
from src.widget import get_data, mask_account_card

VALID_STATUSES = ["EXECUTED", "CANCELED", "PENDING"]


def get_user_input(prompt: str, valid_options: Optional[List[str]] = None) -> str:
    while True:
        user_input = input(prompt).strip().upper()
        if valid_options and user_input not in valid_options:
            print(f"Неверный ввод. Доступные опции: {', '.join(valid_options)}")
        else:
            return user_input


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_option = get_user_input("Введите номер опции: ", ["1", "2", "3"])
    file_path = ''
    if file_option == "1":
        print("Для обработки выбран JSON-файл.")
        file_path = "data/operations.json"
    elif file_option == "2":
        print("Для обработки выбран CSV-файл.")
        file_path = "data/transactions.csv"
    elif file_option == "3":
        print("Для обработки выбран XLSX-файл.")
        file_path = "data/transactions_excel.xlsx"

    try:
        transactions = read_transactions(file_path)
    except Exception as e:
        logger.error(f"Ошибка при чтении файла: {e}")
        print(f"Ошибка при чтении файла: {e}")
        return
    if not transactions:
        print("Не найдено ни одной транзакции в файле.")
        return
    while True:
        status = get_user_input(
            "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ",
            VALID_STATUSES,
        )
        filtered_transactions = filter_by_state(transactions, status)
        if filtered_transactions:
            print(f'Операции отфильтрованы по статусу "{status}"')
        else:
            print(f'Статус операции "{status}" недоступен.')

        sort_option = get_user_input("Отсортировать операции по дате? (Да/Нет): ", ["ДА", "НЕТ"])
        if sort_option == "ДА":
            sort_order = get_user_input(
                "Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ",
                ["ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"],
            )
            ascending = sort_order == "ПО ВОЗРАСТАНИЮ"
            filtered_transactions = sort_by_date(filtered_transactions, ascending)

        rub_option = get_user_input("Выводить только рублевые транзакции? (Да/Нет): ", ["ДА", "НЕТ"])
        if rub_option == "ДА":
            if file_option == "1":
                filtered_json = filter_by_currency(filtered_transactions, "RUB")
                filtered_transactions = list(filtered_json)
            else:
                filtered_transactions = filter_rub_transactions(filtered_transactions)

        desc_option = get_user_input(
            "Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ", ["ДА", "НЕТ"]
        )
        if desc_option == "ДА":
            search_string = input("Введите строку для поиска в описании: ").strip()
            filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

        print("Распечатываю итоговый список транзакций...")

        if not filtered_transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
            break
        else:
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
            for transaction in filtered_transactions:
                date = get_data(transaction["date"])
                description = transaction["description"]
                if file_option == "1":
                    amount = transaction["operationAmount"]["amount"]
                    currency = transaction["operationAmount"]["currency"]["code"]
                else:
                    amount = transaction["amount"]
                    currency = transaction["currency_code"]
                from_account = mask_account_card(transaction.get("from", ""))
                to_account = mask_account_card(transaction["to"])
                print(f"{date} {description}\n{from_account} -> {to_account}\nСумма: {amount} {currency}\n")
            break


if __name__ == "__main__":
    main()
