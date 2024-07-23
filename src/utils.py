import json
import os
from typing import Any, Dict, List


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с данными о финансовых транзакциях и возвращает список словарей.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.

    :param file_path: Путь до JSON-файла
    :return: Список словарей с данными о транзакциях
    """
    if not os.path.exists(file_path):
        print(f"Файл не найден по пути: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print("Содержимое JSON-файла не является списком")
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
    except TypeError:
        print("Неправильный тип данных в JSON-файле")

    return []
