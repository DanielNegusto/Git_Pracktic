import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (1234567812345678, "1234 56** **** 5678"),
        (9876543210987654, "9876 54** **** 7654"),
        (1111222233334444, "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [(64686473678894779589, "**9589"), (35383033474447895560, "**5560"), (73654108430135874305, "**4305")],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
