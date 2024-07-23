import os
from unittest.mock import Mock

import pytest
from dotenv import load_dotenv

from src.external_api import convert_to_rub

# Загрузка переменных окружения из файла .env
load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")


def test_convert_to_rub_with_rub_currency(monkeypatch: Mock) -> None:
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
    monkeypatch.setattr(
        "requests.get", Mock(return_value=Mock(status_code=200, json=Mock(return_value={"result": "100"})))
    )
    assert convert_to_rub(transaction) == 100


def test_convert_to_rub_with_usd_currency(monkeypatch: Mock) -> None:
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    monkeypatch.setattr(
        "requests.get", Mock(return_value=Mock(status_code=200, json=Mock(return_value={"result": "6000"})))
    )
    assert convert_to_rub(transaction) == 6000


def test_convert_to_rub_with_eur_currency(monkeypatch: Mock) -> None:
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}
    monkeypatch.setattr(
        "requests.get", Mock(return_value=Mock(status_code=200, json=Mock(return_value={"result": "6400"})))
    )
    assert convert_to_rub(transaction) == 6400


def test_convert_to_rub_with_unknown_currency(monkeypatch: Mock) -> None:
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "UNKNOWN"}}}
    monkeypatch.setattr(
        "requests.get", Mock(return_value=Mock(status_code=400, json=Mock(return_value={"error": "Unknown error"})))
    )
    with pytest.raises(ValueError):
        convert_to_rub(transaction)
