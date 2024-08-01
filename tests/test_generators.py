from typing import Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 3,
                    "state": "CANCELED",
                    "date": "2021-02-01T11:54:58Z",
                    "amount": 5000.0,
                    "currency_name": "Dollar",
                    "currency_code": "USD",
                    "from": None,
                    "to": "Счет 23294994494356835683",
                    "description": "Перевод организации",
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 2,
                    "state": "EXECUTED",
                    "date": "2021-02-01T11:54:58Z",
                    "amount": 100.0,
                    "currency_name": "Ruble",
                    "currency_code": "RUB",
                    "from": None,
                    "to": "Счет 23294994494356835683",
                    "description": "Перевод со счета на счет",
                },
            ],
        ),
        ("EUR", []),
    ],
)
def test_filter_by_currency(transactions: List[Dict], currency: str, expected: List[Dict]) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


def test_transaction_descriptions(transactions: List[Dict]) -> None:
    expected = ["Открытие вклада", "Перевод со счета на счет", "Перевод организации"]
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
        (0, 0, ["0000 0000 0000 0000"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: list[str]) -> None:
    result = list(card_number_generator(start, end))
    assert result == expected
