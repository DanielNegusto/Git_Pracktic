import json
import os
from typing import Generator
from unittest.mock import patch

import pytest

from src.utils import read_transactions


@pytest.fixture
def setup_files() -> Generator:
    os.makedirs("data", exist_ok=True)
    yield
    # Удаление файлов после тестов
    if os.path.exists("data/test_operations.json"):
        os.remove("data/test_operations.json")
    if os.path.exists("data/empty_operations.json"):
        os.remove("data/empty_operations.json")
    if os.path.exists("data/not_list_operations.json"):
        os.remove("data/not_list_operations.json")
    if os.path.exists("data/invalid_json.json"):
        os.remove("data/invalid_json.json")


def test_read_transactions_success(setup_files: None) -> None:
    data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2020-01-01T12:00:00",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Test transaction",
            "from": "Account 1",
            "to": "Account 2",
        }
    ]
    with open("data/test_operations.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

    transactions = read_transactions("data/test_operations.json")
    assert transactions == data


def test_read_transactions_file_not_found(setup_files: None) -> None:
    # Удаление файла, если он существует, чтобы имитировать его отсутствие
    if os.path.exists("data/non_existing_file.json"):
        os.remove("data/non_existing_file.json")

    transactions = read_transactions("data/non_existing_file.json")
    assert transactions == []


def test_read_transactions_empty_file(setup_files: None) -> None:
    open("data/empty_operations.json", "a").close()
    transactions = read_transactions("data/empty_operations.json")
    assert transactions == []


def test_read_transactions_not_list(setup_files: None) -> None:
    with open("data/not_list_operations.json", "w", encoding="utf-8") as file:
        json.dump({"key": "value"}, file)
    transactions = read_transactions("data/not_list_operations.json")
    assert transactions == []


def test_read_transactions_json_decode_error(setup_files: None) -> None:
    with open("data/invalid_json.json", "w", encoding="utf-8") as file:
        file.write("{invalid json}")
    transactions = read_transactions("data/invalid_json.json")
    assert transactions == []


def test_read_transactions_type_error(setup_files: None) -> None:
    # Создание JSON-файла с некорректными данными для вызова TypeError
    with open("data/invalid_type.json", "w", encoding="utf-8") as file:
        json.dump({"key": "value"}, file)

    with patch("json.load", side_effect=TypeError):
        transactions = read_transactions("data/invalid_type.json")
        assert transactions == []
