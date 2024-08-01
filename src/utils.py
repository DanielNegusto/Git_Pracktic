import json
import os
from typing import Any, Dict, Hashable, List

import pandas as pd

from src.logging_config import logger


def read_transactions(file_path: str) -> list[Any] | list | list[dict[Hashable, Any]]:
    """
    Читает данные о финансовых транзакциях из JSON-, CSV- или XLSX-файла и возвращает список словарей.
    Если файл пустой, содержит не список (в случае JSON) или не найден, возвращает пустой список.

    :param file_path: Путь до файла с данными
    :return: Список словарей с данными о транзакциях
    """
    if not os.path.exists(file_path):
        logger.error(f"Файл не найден по пути: {file_path}")
        return []

    try:
        if file_path.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    logger.warning("Содержимое JSON-файла не является списком")
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path, delimiter=";").dropna()
            return df.to_dict(orient="records")
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path).dropna()
            return df.to_dict(orient="records")
        else:
            logger.error("Неподдерживаемый формат файла")
    except (json.JSONDecodeError, pd.errors.ParserError) as e:
        logger.error(f"Ошибка декодирования или парсинга: {e}")
    except FileNotFoundError:
        logger.error("Файл не найден")
    except TypeError as e:
        logger.error(f"Неправильный тип данных в файле: {e}")
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")

    return []


def save_transactions(transactions: List[Dict[str, Any]], file_path: str) -> None:
    """
    Сохраняет данные о финансовых транзакциях в файл.

    :param transactions: Список словарей с данными о транзакциях
    :param file_path: Путь до файла для сохранения данных
    """
    if not transactions:
        logger.warning("Список транзакций пуст, ничего не сохраняем")
        return

    try:
        if file_path.endswith(".json"):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(transactions, file, ensure_ascii=False, indent=4)
            logger.info(f"Данные успешно сохранены в файл {file_path}")
        elif file_path.endswith(".csv"):
            df = pd.DataFrame(transactions)
            df.to_csv(file_path, index=False, encoding="utf-8")
            logger.info(f"Данные успешно сохранены в файл {file_path}")
        elif file_path.endswith(".xlsx"):
            df = pd.DataFrame(transactions)
            df.to_excel(file_path, index=False)
            logger.info(f"Данные успешно сохранены в файл {file_path}")
        else:
            raise ValueError("Неподдерживаемый формат файла")
    except Exception as e:
        logger.error(f"Ошибка при сохранении данных: {e}")
        raise e
