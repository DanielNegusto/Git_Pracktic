from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(numbers: str) -> str:
    """Получаем строку с номером карты или счёта, возвращаем замаскированную"""
    parts = numbers.split()
    if "Счет" in numbers:
        # Маскировка для счёта
        account_number = int(parts[1])
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}"
    elif len(parts) == 2 or len(parts) == 3:
        # Маскировка для карт
        card_number = int(parts[-1])
        masked_card = get_mask_card_number(card_number)
        if len(parts) == 3:
            return f"{parts[0]} {parts[1]} {masked_card}"
        else:
            return f"{parts[0]} {masked_card}"
    else:
        return "Неверные данные"


def get_data(date_str: str) -> str:
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
