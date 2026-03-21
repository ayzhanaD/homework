import logging
from typing import Union

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s %(filename)s  %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str | None:
    """ функция принимает номер карты и возвращает ее маску"""
    try:
        logger.info(f"Принимаем номер карты: {card_number}")
        card_number = str(card_number)
        card_mask = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return card_mask
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


def get_mask_account(account_number: Union[int, str]) -> str | None:
    """ функция принимает номер счета и возвращает его маску"""
    try:
        logger.info(f"Принимаем номер счета: {account_number}")
        account_number = str(account_number)
        account_mask = f"**{account_number[-4:]}"
        return account_mask
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
