import csv

import pandas as pd


def read_csv_file(csv_file: str) -> list:
    """ функция принимает путь к csv файлу и выводит его содержимое """
    transactions = []

    with open(csv_file) as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            transactions.append(row)

    return transactions


def read_excel_file(excel_file: str) -> list:
    """ функция принимает путь к excel файлу и выводит его содержимое """
    with open(excel_file, "rb") as file:
        transactions = pd.read_excel(file).to_dict(orient='records')
        return transactions
