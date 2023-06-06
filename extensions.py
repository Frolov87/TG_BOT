
from config import keys #Импортируем словарь валют из файла config

import requests #Импортируем библиотеку для получения данных с API
import json #Импортируем библиотеку для преобразования полученных данных в удобный формат

class ConvertionException(Exception): # Создаем класс исключений
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f"Невозможно перевести {base} в {base}")

        try:
            quote_ticker = keys[quote]

        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}")


# Получаем данные с API, переводим в нужный формат и возвращаем результат
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]
        return total_base


