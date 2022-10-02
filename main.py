import telebot
from key import keys, TOKEN
from ConvertionException import ConvertionException, TelegramConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def start(message: telebot.types.Message):
    text = f'Чтобы начать работу введите комманду боту в следующем формате:'
    f'\n<имя валюты> <в какую валюту перевести> <количество переводимой валюты>'
    f'\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")

    if len(values) != 3:
        raise ConvertionException(f"Что-то много информации, можно чуть-чуть поменьше")

    base, currency, amount = values
    total_currency = TelegramConverter.convert(base, currency, amount)

    text = f"Цена {amount} {base} в {currency} - {total_currency}"
    bot.send_message(message.chat.id, text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.polling(none_stop=True)
