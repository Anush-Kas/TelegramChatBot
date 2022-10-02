import requests
import json
from key import keys

class ConvertionException(Exception):
    pass


class TelegramConverter:
    @staticmethod
    def convert(base: str, currency: str, amount: str):
        if base == currency:
            raise ConvertionException("Мне кажется ты знаешь ответ на этот запрос)")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не понятная валюта {base} для меня")

        try:
            currency_ticker = keys[currency]
        except KeyError:
            raise ConvertionException(f"Не понятна валюта {currency} для меня")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Мне кажется это {amount} не похоже на цифру")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={currency_ticker}")
        total_currency = json.loads(r.content)[keys[currency]]
