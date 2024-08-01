import re
from typing import Any, Dict, List, Optional

from src.widget import get_data


def filter_by_state(records: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    records: Список словарей, где каждый содержит ключ 'state'.
    state: Значение для фильтрации по ключу 'state'. По умолчанию 'EXECUTED'.
    Возвращает новый список словарей, содержащий только те, у которых значение 'state' соответствует указанному.
    """
    return [el for el in records if el.get("state") == state]


def sort_by_date(records: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по значению ключа 'date'.
    records: Список словарей, где каждый содержит ключ 'date'.
    descending: Порядок сортировки. True для убывания, False для возрастания. По умолчанию True.
    Возвращает новый список словарей, отсортированный по дате.
    """
    return sorted(records, key=lambda el: get_data(el["date"]), reverse=not descending)


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории.

    :param transactions: Список словарей с данными о транзакциях
    :param categories: Список категорий операций
    :return: Словарь с количеством операций в каждой категории
    """
    category_counts = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
                break  # Предполагаем, что каждая операция принадлежит только одной категории

    return category_counts


def filter_transactions_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций, возвращая только те, у которых в описании есть заданная строка поиска.

    :param transactions: Список словарей с данными о транзакциях
    :param search_string: Строка поиска
    :return: Отфильтрованный список транзакций
    """
    filtered_transactions = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    for transaction in transactions:
        description = transaction.get("description", "")
        if pattern.search(description):
            filtered_transactions.append(transaction)

    return filtered_transactions


def filter_rub_transactions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [t for t in transactions if t["currency_code"] == "RUB"]
