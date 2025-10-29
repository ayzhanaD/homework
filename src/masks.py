from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """ функция принимает номер карты и возвращает ее маску"""
    card_number = str(card_number)
    card_mask = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return card_mask


def get_mask_account(account_number: Union[int, str]) -> str:
    """ функция принимает номер счета и возвращает его маску"""
    account_number = str(account_number)
    account_mask = f"**{account_number[-4:]}"
    return account_mask
