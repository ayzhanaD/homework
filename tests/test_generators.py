import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[dict]) -> None:
    # USD currency tests
    usd_transactions = filter_by_currency(transactions, "USD")

    assert next(usd_transactions) == {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
    }

    assert next(usd_transactions) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
    }

    # RUB currency test
    rub_transactions = filter_by_currency(transactions, "RUB")

    assert next(rub_transactions) == {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
    }

    # EUR(not in list) currency test
    eur_currency_transactions = filter_by_currency(transactions, "EUR")

    assert next(eur_currency_transactions) == "транзакции отсутствуют"

    # empty list test
    empty_currency_transactions = filter_by_currency([], "USD")

    assert next(empty_currency_transactions) == "транзакции отсутствуют"


def test_transaction_descriptions(transactions: list[dict]) -> None:
    description = transaction_descriptions(transactions)

    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"

    assert next(transaction_descriptions([])) == "транзакции отсутствуют"


@pytest.mark.parametrize("start, end, expected", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]),
    (99991, 99995, [
        "0000 0000 0009 9991",
        "0000 0000 0009 9992",
        "0000 0000 0009 9993",
        "0000 0000 0009 9994",
        "0000 0000 0009 9995",
    ]),
    (1111111111111111, 1111111111111115, [
        "1111 1111 1111 1111",
        "1111 1111 1111 1112",
        "1111 1111 1111 1113",
        "1111 1111 1111 1114",
        "1111 1111 1111 1115",
    ]),
    (9999999999999991, 9999999999999995, [
        "9999 9999 9999 9991",
        "9999 9999 9999 9992",
        "9999 9999 9999 9993",
        "9999 9999 9999 9994",
        "9999 9999 9999 9995"
    ])
])
def test_card_number_generator(start: int, end: int, expected: list[str]) -> None:
    assert list(card_number_generator(start, end)) == expected
