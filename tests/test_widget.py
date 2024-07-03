import pytest
from datetime import datetime
from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счёт 35383033474447895560", "Счет **5560"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", "Неверные данные")
    ],
)
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2018-07-11T02:26:18.671407", datetime(2018, 7, 11, 2, 26, 18, 671407)),
    ("2019-12-31T23:59:59.999999", datetime(2019, 12, 31, 23, 59, 59, 999999)),
    ("2020-01-01T00:00:00.000000", datetime(2020, 1, 1, 0, 0, 0, 0)),
    ("2021-05-15T12:30:45.123456", datetime(2021, 5, 15, 12, 30, 45, 123456))
])
def test_get_data(date_str, expected):
    assert get_data(date_str) == expected
