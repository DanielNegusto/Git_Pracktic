def get_mask_card_number(numbers_card: int) -> str:
    """Получаем номер карты, возвращаем замаскированный"""
    str_number = str(numbers_card)
    mask_number = str_number[0:4] + " " + str_number[4:6] + "** ****" + " " + str_number[-4:]
    return mask_number


def get_mask_account(numbers_account: int) -> str:
    """Получаем номер счёта, возвращаем замаскированный"""
    str_number = str(numbers_account)
    mask_account = "**" + str_number[-4:]
    return mask_account


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
