import telebot
from telebot import types
from collections import defaultdict

bot = telebot.TeleBot('898491912:AAEmzXCPpJW8RY5gvq-vPdVzWobjZBJ9wOQ')

keyboard1 = telebot.types.ReplyKeyboardMarkup()  # обращение к библиотеке
keyboard1.row('хочу')  # строка с кнопками
keyboard1.row('Отстань')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты хочешь увидеть пингвинов?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def message_penguine(message):
    if message.text == 'хочу':
        bot.send_message(message.chat.id,    '_-_\n'
                                           ' (o o)\n'
                                           '/  V  \ \n'
                                          '/(  _  )\ '
                                          '\n^^ ^^')


if name == 'main':
    bot.polling()