import telebot
from key import keys, TOKEN
from extensions import Conversion, ConversionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message: telebot.types.Message):
    text = f'Добро пожаловать {message.from_user.first_name}!' \
            f'\nЧтобы начать работу введите команду боту в следующем формате:' \
            f'\nUSD RUB 10' \
            f'\nУвидеть список всех доступных валют можно командой: /values' \
            f'\nЕсли у вас возникнут вопросы, вы можете воспользоваться командой: /help'

    bot.reply_to(message, text)


@bot.message_handler(commands=["help"])
def start(message: telebot.types.Message):
    text = f'\nЧтобы начать работу введите команду боту в следующем формате:' \
           f'\nUSD RUB 10' \
           f'\nЧтобы увидеть список всех доступных валют можно воспользоваться командой: /values'

    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def keys(message: telebot.types.Message):
    text = f'Доступные валюты:' \
           f'\n<b>RUB</b> - Российский рубль;\n<b>USD</b> - Доллар США;' \
           f'\n<b>EUR</b> - Евро;\nЗдесь приведены только три валютные пары, ' \
           f'но можно использовать и любые другие валютные коды интересующих ' \
           f'вас валютных пар.'
    bot.reply_to(message, text, parse_mode='html')


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise ConversionException(f'Не понятен формат запроса' 
                                      f'\nПосмотреть помощь: /help'
                                      )

        base, quote, amount = values
        text = Conversion.convert(base.upper(), quote.upper(), amount)
    except ConversionException as e:
        bot.reply_to(message, f'Дорогой {message.from_user.first_name} у вас ошибка:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Этот виртуальный мир не понимает что ты хочешь:\n{e}')
    else:
        bot.send_message(message.chat.id, text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.infinity_polling()
