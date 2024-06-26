def mask_account_card(numbers: str) -> str:
    """Получаем номер карты или счёта, возвращаем замаскированный"""
    parts = numbers.split()
    if "Счет" in numbers:
        # Маскировка для счёта
        account_number = numbers.split("Счет ")[1]
        masked_account = "**" + account_number[-4:]
        return f"Счёт {masked_account}"
    elif len(parts) == 2 or len(parts) == 3:
        # Маскировка для карт
        number = parts[-1]
        masked_number = number[:4] + " " + number[4:6] + "** **** " + number[-4:]
        if len(parts) == 3:
            return f"{parts[0]} {parts[1]} {masked_number}"
        else:
            return f"{parts[0]} {masked_number}"
    else:
        return "Неверные данные"


def get_data(date_str: str) -> str:
    date_part = date_str.split("T")[0]
    print(date_part)
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


inputs = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]


masked_outputs = [mask_account_card(numbers) for numbers in inputs]
for numbers in masked_outputs:
    print(numbers)

print(get_data("2018-07-11T02:26:18.671407"))
