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


example_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Фильтрация данных по статусу 'EXECUTED'
filtered_data = filter_by_state(example_data)
print("Фильтрация по статусу (EXECUTED):")
for record in filtered_data:
    print(record)

# Сортировка данных по дате в убывающем порядке
sorted_data = sort_by_date(example_data)
print("\nСортировка в убывающем порядке:")
for record in sorted_data:
    print(record)

# Сортировка данных по дате в возрастающем порядке
sorted_data_asc = sort_by_date(example_data, False)
print("\nСортировка в возрастающем порядке:")
for record in sorted_data_asc:
    print(record)
