from typing import Any, Dict, List

import pytest


@pytest.fixture
def transactions() -> List[Dict]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2021-02-01T11:54:58Z",
            "amount": 23789.0,
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": None,
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2021-02-01T11:54:58Z",
            "amount": 100.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": None,
            "to": "Счет 23294994494356835683",
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": 5000.0,
            "currency_name": "Dollar",
            "currency_code": "USD",
            "from": None,
            "to": "Счет 23294994494356835683",
            "description": "Перевод организации",
        },
    ]


@pytest.fixture
def example_data() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sample_transaction_rub() -> Dict[str, Any]:
    return {
        "id": 2,
        "state": "EXECUTED",
        "date": "2020-01-01T12:00:00",
        "operationAmount": {"amount": "5000.00", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Test transaction",
        "from": "Account 1",
        "to": "Account 2",
    }


@pytest.fixture
def transaction_usd() -> Dict[str, Any]:
    return {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}


@pytest.fixture
def transaction_rub() -> Dict[str, Any]:
    return {"operationAmount": {"amount": "5000.00", "currency": {"code": "RUB"}}}
