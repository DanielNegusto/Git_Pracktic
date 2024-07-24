from typing import Optional

from src.logging_config import logger


def get_mask_card_number(numbers_card: Optional[str] = None) -> Optional[str]:
    """Получаем номер карты, возвращаем замаскированный"""
    if numbers_card and numbers_card.isdigit():
        try:
            mask_number = numbers_card[0:4] + " " + numbers_card[4:6] + "** ****" + " " + numbers_card[-4:]
            logger.info(f"Замаскированный номер карты: {numbers_card}: {mask_number}")
            return mask_number
        except Exception as e:
            logger.error(f"Ошибка при замаскировке номера карты: {e}")
            return None
    else:
        logger.warning(f"Номер карты пустой или неправильный номер карты: {numbers_card}")
        return None


def get_mask_account(numbers_account: Optional[str] = None) -> Optional[str]:
    """Получаем номер счёта, возвращаем замаскированный"""
    try:
        if not numbers_account or not numbers_account.isdigit():
            raise ValueError("Номер счёта должен быть не пустой строкой и состоять только из цифр")
        mask_account = "**" + numbers_account[-4:]
        logger.info(f"Замаскированный номер счёта: {numbers_account}: {mask_account}")
        return mask_account
    except ValueError as ve:
        logger.error(f"Ошибка: {ve}")
        return None
    except Exception as e:
        logger.error(f"Ошибка при замаскировке номера счёта: {e}")
        return None
