import os
from typing import Any, Dict
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.external_api import convert_to_rub

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get: Any, transaction_usd: Dict[str, Any]) -> None:
    # Настройка мока для успешного ответа
    mock_response = {"result": "7500.00"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Вызов функции
    result = convert_to_rub(transaction_usd)

    # Проверка результата
    assert result == 7500.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        params={"to": "RUB", "from": "USD", "amount": "100.0"},
        headers={"apikey": API_KEY},
    )


def test_convert_to_rub_rub(transaction_rub: Dict[str, Any]) -> None:
    # Вызов функции без мока, так как RUB не требует внешнего вызова
    result = convert_to_rub(transaction_rub)

    # Проверка результата
    assert result == 5000.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get: Any, transaction_usd: Dict[str, Any]) -> None:
    # Настройка мока для ответа с ошибкой
    mock_response = {"error": "API error"}
    mock_get.return_value.status_code = 400
    mock_get.return_value.json.return_value = mock_response

    with pytest.raises(ValueError, match="Error in API request: API error"):
        convert_to_rub(transaction_usd)
