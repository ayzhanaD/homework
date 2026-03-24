from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[str | dict, Any, None]:
    """  функция принимает список транзакций и возвращает транзакции, соответствующие заданной валюте """
    try:
        filtered_transactions: list[dict] = (
            list(filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == currency_code,
                        transactions))
        )
    except KeyError:
        filtered_transactions: list[dict] = (
            list(filter(lambda transaction: transaction["currency_code"] == currency_code, transactions))
        )

    if len(filtered_transactions) < 1:
        yield "транзакции отсутствуют"

    transaction_index = 0
    while transaction_index < len(filtered_transactions):
        yield filtered_transactions[transaction_index]
        transaction_index += 1


def transaction_descriptions(transactions: list[dict]) -> Generator[str | dict, None, None]:
    """  функция принимает список транзакций и возвращает описание каждой операции """
    descriptions: list[dict] = list(map(lambda transaction: transaction["description"], transactions))

    if len(descriptions) < 1:
        yield "транзакции отсутствуют"

    transaction_index = 0
    while transaction_index < len(transactions):
        yield descriptions[transaction_index]
        transaction_index += 1


def card_number_generator(start_number: int, end_number: int) -> Generator[str, Any, None]:
    """ функция генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX """

    while start_number <= end_number:
        if len(str(start_number)) < 16:
            zeros_count = 16 - len(str(start_number))
            card_number = f"{"0" * zeros_count}" + str(start_number)
            yield (f"{card_number[0:4]} "
                   f"{card_number[4:8]} "
                   f"{card_number[8:12]} "
                   f"{card_number[12:16]}")
        elif len(str(start_number)) == 16:
            str_start_number = str(start_number)
            yield (f"{str_start_number[0:4]} "
                   f"{str_start_number[4:8]} "
                   f"{str_start_number[8:12]} "
                   f"{str_start_number[12:16]}")
        start_number += 1
