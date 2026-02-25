import json
import logging
from typing import Any

from external_api import convert_currency

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s %(filename)s  %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions(json_file: str) -> Any:
    """ функция ожидает получить путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях """

    if not json_file:
        logger.info("JSON-файл не найден")
        return []

    try:
        try:
            logger.info(f"Читаем JSON-файл: {json_file}")
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)
        except UnicodeDecodeError as e:
            logger.error(f"Произошла ошибка: {e}")

        return data
    except json.JSONDecodeError:
        logger.info("JSON-файл не найден")
        return []


def get_transaction_amount(transaction: dict) -> Any:
    """ функция принимает транзакцию и возвращает сумму транзакции в рублях, если
    транзакция была в USD или в EUR конвертирует сумму операции в рубли """

    try:
        transaction_currency_code = transaction["operationAmount"]["currency"]["code"]
        transaction_amount = transaction["operationAmount"]["amount"]
        logger.info(f"Извлекаем валюту транзакции: {transaction_currency_code}")
        logger.info(f"Извлекаем сумму транзакции: {transaction_amount}")

        if transaction_currency_code == "USD" or transaction_amount == "EUR":
            logger.info("Проверяем необходимость конвертации валюты в рубли")
            return convert_currency(transaction_amount, transaction_currency_code)
        else:
            logger.info("Возвращаем сумму транзакции в рублях")
            return float(transaction_amount)
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
