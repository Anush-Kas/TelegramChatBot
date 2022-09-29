import telebot
import requests
import json
import key


bot = telebot.TeleBot(key.TOKEN)

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.polling(none_stop=True)