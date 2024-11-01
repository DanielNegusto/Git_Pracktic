from datetime import datetime

from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(numbers: str) -> str:
    """Получаем строку с номером карты или счёта, возвращаем замаскированную"""
    normalized_numbers = numbers.replace("ё", "е").lower()  # Нормализуем строку
    parts = numbers.split()
    if "счет" in normalized_numbers:
        # Маскировка для счёта
        account_number = parts[1]
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}"
    elif len(parts) == 2 or len(parts) == 3:
        # Маскировка для карт
        card_number = parts[-1]
        masked_card = get_mask_card_number(card_number)
        if len(parts) == 3:
            return f"{parts[0]} {parts[1]} {masked_card}"
        else:
            return f"{parts[0]} {masked_card}"
    else:
        return "Неверные данные"


def get_data(date_str: str) -> str:
    date = datetime.fromisoformat(date_str)
    return date.strftime("%d.%m.%Y")
