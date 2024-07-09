from typing import Dict, Iterator, List


def filter_by_currency(transit: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте.
    currency: Код валюты для фильтрации (например, 'USD').
    Возвращает итератор, который поочередно выдаёт транзакции, где валюта соответствует заданной.
    """
    return (el for el in transit if el.get("operationAmount", {}).get("currency", {}).get("code") == currency)


def transaction_descriptions(transact: List[Dict]) -> Iterator[str]:
    """
    Генерирует описания транзакций по очереди.
    Возвращает итератор, который поочередно выдаёт описания транзакций.
    """
    for el in transact:
        yield el.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    for number in range(start, end + 1):
        # Преобразуем число в строку и дополняем нулями слева до 16
        number_str = f"{number:016d}"
        # Форматируем строку в формате XXXX XXXX XXXX XXXX
        formatted_number = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:16]}"
        yield formatted_number
