import telebot

from config import *
from extensions import Converter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Приветствую! Какую информацию по текущему курсу валют вы хотите узнать?"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        comands = message.text.split()
        if len(comands) != 3:
            raise ValueError('Неверное количество параметров')
        base, sym, amount = comands
        new_price = Converter.get_price(base, sym, amount)
        bot.reply_to(message, f"Цена {amount} {base} в {sym} : {new_price}")
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}" )

bot.polling()