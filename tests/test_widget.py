import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счёт 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected
