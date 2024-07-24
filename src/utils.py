import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с данными о финансовых транзакциях и возвращает список словарей.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.

    :param file_path: Путь до JSON-файла
    :return: Список словарей с данными о транзакциях
    """
    if not os.path.exists(file_path):
        logger.error(f"Файл не найден по пути: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Получен список транзакций")
                return data
            else:
                logger.error("Содержимое JSON-файла не является списком")
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
    except TypeError:
        logger.error("Неправильный тип данных в JSON-файле")

    return []
