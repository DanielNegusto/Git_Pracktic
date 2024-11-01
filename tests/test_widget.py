from datetime import datetime

import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счёт 35383033474447895560", "Счет **5560"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", "Неверные данные"),
    ],
)
def test_mask_account_card(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-12-31T23:59:59.999999", "31.12.2019"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("2021-05-15T12:30:45.123456", "15.05.2021"),
    ],
)
def test_get_data(date_str: str, expected: datetime) -> None:
    assert get_data(date_str) == expected
