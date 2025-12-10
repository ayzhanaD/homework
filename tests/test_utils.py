from src.utils import get_transaction_amount, get_transactions


def test_get_transactions() -> None:
    assert get_transactions("") == []


def test_get_transaction_amount() -> None:
    assert get_transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ) == 31957.58
