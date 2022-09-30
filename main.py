import telebot
import requests
import json
from key import TOKEN


bot = telebot.TeleBot(TOKEN)

keys = {
        "рубль" : "RUB",
        "доллар" : "USD",
        "евро" : "EUR",
        }


@bot.message_handler(commands=["start", "help"])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")

    if len(values) > 3:
        raise ConvertionException(f"Что-то много информации, можно чуть-чуть поменьше")

    base, currency, amount = values

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
    text = f"Цена {amount} {base} в {currency} - {float(amount) * total_currency}"
    bot.send_message(message.chat.id, text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.polling(none_stop=True)