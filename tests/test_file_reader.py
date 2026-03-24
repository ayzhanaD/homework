from src.file_reader import read_csv_file, read_excel_file


def test_read_csv_file() -> None:
    first_item = read_csv_file("data/transactions.csv")[0]
    assert first_item == {
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210', 'currency_name':
            'Sol', 'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
    }


def test_read_excel_file() -> None:
    first_item = read_excel_file("data/transactions_excel.xlsx")[0]
    assert first_item == {
            'id': 650703.0,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210.0, 'currency_name':
            'Sol', 'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
    }
