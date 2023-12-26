from algo import get_words
import telebot
from telebot import types

BOT_TOKEN = '6790284577:AAHb21_efi8q9JRoEIdI_ZeGVX48Og1Uyns'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сгенерировать новую фразу")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Здравствуйте!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Сгенерировать новую фразу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сгенерировать новую фразу")
        btn2 = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, get_words(), reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сгенерировать новую фразу")
        btn2 = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2)
        text = 'Данный бот умеет генерировать случайные фразы. Для того чтобы бот сгенерировал новую фразу, нажмите на кнопку "Сгенерировать новую фразу".'
        bot.send_message(message.chat.id, text, reply_markup=markup)


bot.infinity_polling()