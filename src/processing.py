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
    return sorted(records, key=lambda el: get_data(el["date"]), reverse=descending)
