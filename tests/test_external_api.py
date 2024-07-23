import os
from typing import Any, Dict
from unittest.mock import patch, MagicMock

import pytest
from dotenv import load_dotenv

from src.external_api import convert_to_rub, get_transaction_amount_in_rub

# Загрузка переменных окружения из файла .env
load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")


@patch("src.external_api.requests.get")
def test_convert_to_rub_success(mock_get: MagicMock) -> None:
    # Настроить моки для успешного ответа
    mock_response = {"result": "7500.00"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Вызов функции
    result = convert_to_rub(100.0, "USD")

    # Проверка результата
    assert result == 7500.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        params={"to": "RUB", "from": "USD", "amount": "100.0"},
        headers={"apikey": API_KEY},
    )


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get: MagicMock) -> None:
    # Настроить моки для ошибки API
    mock_response = {"error": "Invalid API key"}
    mock_get.return_value.status_code = 400
    mock_get.return_value.json.return_value = mock_response

    # Вызов функции и проверка исключения
    with pytest.raises(ValueError, match="Error in API request: Invalid API key"):
        convert_to_rub(100.0, "USD")

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        params={"to": "RUB", "from": "USD", "amount": "100.0"},
        headers={"apikey": API_KEY},
    )


def test_get_transaction_amount_in_rub_rub(sample_transaction_rub: Dict[str, Any]) -> None:
    result = get_transaction_amount_in_rub(sample_transaction_rub)
    assert result == 5000.0
