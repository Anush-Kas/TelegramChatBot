import requests
import json
from key import keys


class ConversionException(Exception):
    pass


class Conversion:
    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if base == quote:
            raise ConversionException("Мне кажется ты знаешь ответ на этот вопрос)"
                                      f'\nУзнать другие возможности можно командой: /help')

        if len(base) != 3 and len(quote) != 3:
            raise ConversionException(f'Не понятный код валюты "{base}" и "{quote}" для меня.'
                                      f'\nПосмотреть помощь: /help'
                                      )
        elif len(base) != 3:
            raise ConversionException(f'Не понятный код валюты "{base}" для меня.'
                                      f'\nПосмотреть помощь: /help'
                                      )
        elif len(quote) != 3:
            raise ConversionException(f'Не понятный код валюты "{quote}" для меня.'
                                      f'\nПосмотреть помощь: /help'
                                      )
        elif base.isnumeric() or quote.isnumeric():
            raise ConversionException(f'Код валюты не может быть цифрами'
                                      f'\nПосмотреть помощь: /help'
                                      )
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Мне кажется это "{amount}" не похоже на цифру'
                                      f'\nПосмотреть помощь: /help'
                                      )

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}")
        total_currency = json.loads(r.content)[quote]
        text = f'Цена {amount} {base} в {quote} - {amount * total_currency}'
        return text

