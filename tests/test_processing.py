from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


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
                "2018-10-14T08:21:33.419441",
                "2018-09-12T21:27:25.241689",
                "2018-06-30T02:08:58.425572",
            ],
        ),
        (
            False,
            [
                "2018-06-30T02:08:58.425572",
                "2018-09-12T21:27:25.241689",
                "2018-10-14T08:21:33.419441",
                "2019-07-03T18:35:29.512364",
            ],
        ),
    ],
)
def test_sort_by_date(example_data: List[Dict[str, Any]], descending: bool, expected_dates: List[str]) -> None:
    sorted_data = sort_by_date(example_data, descending)
    assert [record["date"] for record in sorted_data] == expected_dates
