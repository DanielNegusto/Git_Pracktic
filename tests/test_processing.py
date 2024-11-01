from typing import Any, Dict, List

import pytest

from src.processing import (count_transactions_by_category, filter_by_state, filter_rub_transactions,
                            filter_transactions_by_description, sort_by_date)


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("PENDING", []),
    ],
)
def test_filter_by_state(example_data: List[Dict[str, Any]], state: str, expected: List[Dict[str, Any]]) -> None:
    assert filter_by_state(example_data, state) == expected


@pytest.mark.parametrize(
    "descending, expected_dates",
    [
        (
            True,
            [
                "2019-07-03T18:35:29.512364",
                "2018-09-12T21:27:25.241689",
                "2018-10-14T08:21:33.419441",
                "2018-06-30T02:08:58.425572",
            ],
        ),
        (
            False,
            [
                "2018-06-30T02:08:58.425572",
                "2018-10-14T08:21:33.419441",
                "2018-09-12T21:27:25.241689",
                "2019-07-03T18:35:29.512364",
            ],
        ),
    ],
)
def test_sort_by_date(example_data: List[Dict[str, Any]], descending: bool, expected_dates: List[str]) -> None:
    sorted_data = sort_by_date(example_data, descending)
    assert [record["date"] for record in sorted_data] == expected_dates


categories = ["Открытие вклада", "Перевод со счета на счет", "Перевод организации"]


# Тесты
def test_count_transactions_by_category(transactions: List[Dict]) -> None:
    expected_counts = {"Открытие вклада": 1, "Перевод со счета на счет": 1, "Перевод организации": 1}
    assert count_transactions_by_category(transactions, categories) == expected_counts


def test_filter_transactions_by_description(transactions: List[Dict]) -> None:
    search_string = "Перевод"
    expected_filtered = [
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
    ]
    assert filter_transactions_by_description(transactions, search_string) == expected_filtered


def test_filter_rub_transactions(transactions: List[Dict]) -> None:
    expected_filtered = [
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
        }
    ]
    assert filter_rub_transactions(transactions) == expected_filtered
