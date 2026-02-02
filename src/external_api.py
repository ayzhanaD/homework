import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(amount: float, currency_code: str) -> float | str:
    """ функция принимает сумму и код валюты, обращается к внешнему API
    для конвертации валюты в RUB и возвращает результат """

    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=rub&from={currency_code}&amount={amount}"

        headers = {
            "apikey": os.getenv("API_KEY")
        }

        response = requests.get(url, headers)

        result = response.json()
        return float(result["result"])
    except requests.exceptions.RequestException:
        return "error occurred"
