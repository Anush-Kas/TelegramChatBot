class ConvertionException(Exception):
    if len(values) > 3:
        raise ConvertionException(f"Что-то много информации, можно чуть-чуть поменьше")

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