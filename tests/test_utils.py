import json
import os
from typing import Generator

import pandas as pd
import pytest

from src.utils import read_transactions, save_transactions


@pytest.fixture
def setup_files() -> Generator:
    os.makedirs("data", exist_ok=True)
    yield
    for file in [
        "test_operations.json",
        "test_operations.csv",
        "test_operations.xlsx",
        "invalid_csv.csv",
        "invalid_json.json",
        "invalid_xlsx.xlsx",
    ]:
        if os.path.exists(f"data/{file}"):
            os.remove(f"data/{file}")


def test_read_transactions_json(setup_files: Generator) -> None:
    data = [{"id": 1, "state": "EXECUTED"}]
    with open("data/test_operations.json", "w", encoding="utf-8") as file:
        json.dump(data, file)
    transactions = read_transactions("data/test_operations.json")
    assert transactions == data


def test_read_transactions_csv(setup_files: Generator) -> None:
    data = "id;state\n1;EXECUTED\n"
    with open("data/test_operations.csv", "w", encoding="utf-8") as file:
        file.write(data)
    transactions = read_transactions("data/test_operations.csv")
    assert transactions == [{"id": "1", "state": "EXECUTED"}]


def test_read_transactions_xlsx(setup_files: Generator) -> None:
    data = pd.DataFrame([{"id": 1, "state": "EXECUTED"}])
    data.to_excel("data/test_operations.xlsx", index=False)
    transactions = read_transactions("data/test_operations.xlsx")
    assert transactions == [{"id": 1, "state": "EXECUTED"}]


def test_read_transactions_file_not_found(setup_files: Generator) -> None:
    transactions = read_transactions("data/non_existing_file.json")
    assert transactions == []


def test_read_transactions_invalid_json(setup_files: Generator) -> None:
    with open("data/invalid_json.json", "w", encoding="utf-8") as file:
        file.write("{invalid json}")
    transactions = read_transactions("data/invalid_json.json")
    assert transactions == []
    os.remove("data/invalid_json.json")


def test_read_transactions_invalid_csv(setup_files: Generator) -> None:
    data = "id;state\n1;EXECUTED\ninvalid_line"
    with open("data/invalid_csv.csv", "w", encoding="utf-8") as file:
        file.write(data)
    transactions = read_transactions("data/invalid_csv.csv")
    assert transactions == [{"id": "1", "state": "EXECUTED"}]


def test_read_transactions_invalid_xlsx(setup_files: Generator) -> None:
    with open("data/invalid_xlsx.xlsx", "w", encoding="utf-8") as file:
        file.write("invalid data")
    transactions = read_transactions("data/invalid_xlsx.xlsx")
    assert transactions == []
    os.remove("data/invalid_xlsx.xlsx")


def test_save_transactions_json(setup_files: Generator) -> None:
    transactions = [{"id": 1, "state": "EXECUTED"}]
    save_transactions(transactions, "data/test_operations.json")
    with open("data/test_operations.json", "r", encoding="utf-8") as file:
        saved_data = json.load(file)
    assert saved_data == transactions


def test_save_transactions_csv(setup_files: Generator) -> None:
    transactions = [{"id": 1, "state": "EXECUTED"}]
    save_transactions(transactions, "data/test_operations.csv")
    df = pd.read_csv("data/test_operations.csv")
    saved_data = df.to_dict(orient="records")
    assert saved_data == transactions


def test_save_transactions_xlsx(setup_files: Generator) -> None:
    transactions = [{"id": 1, "state": "EXECUTED"}]
    save_transactions(transactions, "data/test_operations.xlsx")
    df = pd.read_excel("data/test_operations.xlsx")
    saved_data = df.to_dict(orient="records")
    assert saved_data == transactions


def test_save_transactions_empty(setup_files: Generator) -> None:
    save_transactions([], "data/test_operations.json")
    assert not os.path.exists("data/test_operations.json")


def test_save_transactions_unsupported_format(setup_files: Generator) -> None:
    transactions = [{"id": 1, "state": "EXECUTED"}]

    with pytest.raises(ValueError, match="Неподдерживаемый формат файла"):
        save_transactions(transactions, "data/test_operations.unsupported")
