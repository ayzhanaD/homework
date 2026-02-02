import json
from typing import Any

from external_api import convert_currency


def get_transactions(json_file: str) -> Any:
    """ функция ожидает получить путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях """

    if not json_file:
        return []

    try:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
        except UnicodeDecodeError:
            with open(json_file, 'r', encoding='cp1252') as f:
                data = json.load(f)


        return data
    except json.JSONDecodeError:
        return []


def get_transaction_amount(transaction: dict) -> Any:
    """ функция принимает транзакцию и возвращает сумму транзакции в рублях, если
    транзакция была в USD или в EUR конвертирует сумму операции в рубли """

    transaction_currency_code = transaction["operationAmount"]["currency"]["code"]
    transaction_amount = transaction["operationAmount"]["amount"]

    if transaction_currency_code == "USD" or transaction_amount == "EUR":
        return convert_currency(transaction_amount, transaction_currency_code)
    else:
        return float(transaction_amount)
