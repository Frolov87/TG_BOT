
import telebot  #Импортирует библиотеку

from config import keys, TOKEN  #Импортируем keys, TOKEN из файла config

from extensions import ConvertionException, CryptoConverter  #Импортируем исключения из файла extensions

bot = telebot.TeleBot(TOKEN)  #Создаем бота



@bot.message_handler(commands=['help'])  #Создаем обработчик команды help
def help(message):
    bot.reply_to(message, "Команда /values: Выводит список доступных валют\nКоманда /start: Запускает программу")

@bot.message_handler(commands=['start'])  ##Создаем обработчик команды start
def start(message):
    bot.reply_to(message,"Введите валюту из которой нужно конвертировать\nВведите валюту в которую нужно конвертировать\nВведите необходимую сумму\nПример: доллар рубль 100\nСписок доступных валют: /values")

@bot.message_handler(commands=['values'])  #Создаем обработчик команды values и выводим валюты в столбик
def values(message):
    text= "Список доступных валют:"
    for key in keys:
        text='\n'.join((text,key))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text'])  #Создаем обработчик приветствия, отвечающий на любой текст
def send_welcome(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}.\nПолучи инструкцию введя или нажав на команды /start или /help")

@bot.message_handler(content_types=['text'])  ##Создаем обработчик конвертации
def convert(message):
    try:
        values = message.text.split(' ') #Создаем значения

        if len(values) !=3: # пишем условие и ошибку за несоблюдение
            raise ConvertionException("Ошибка ввода параметров")
        quote,base,amount = values  #Присваиваем значения к условию
        total_base =CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:  #Если условие соблюдается, выводим код
        text =  f"Цена{amount}{quote} в {base}: {total_base}"
        bot.send_message(message.chat.id,text)









bot.polling(none_stop=True)


