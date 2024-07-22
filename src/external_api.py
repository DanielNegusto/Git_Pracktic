import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму из заданной валюты в рубли.

    :param transaction: Словарь транзакции
    :return: Сумма в рублях
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    params = {"to": "RUB", "from": currency, "amount": str(amount)}

    headers = {"apikey": API_KEY}

    response = requests.get(API_URL, params=params, headers=headers)
    response_data = response.json()

    if response.status_code == 200:
        return float(response_data["result"])
    else:
        error_message = response_data.get("error", "Unknown error")
        raise ValueError(f"Error in API request: {error_message}")
