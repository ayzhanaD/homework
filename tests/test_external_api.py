import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import convert_currency

load_dotenv()

headers = {
    "apikey": os.getenv("API_KEY")
}


def test_convert_currency() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 50244.7827}
        assert convert_currency(555.0, "EUR") == 50244.7827
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=rub&from=EUR&amount=555.0",
            headers)
    # api - истекла бесплатная подписка
    # assert convert_currency(555.0, "RUB") == 555.0
