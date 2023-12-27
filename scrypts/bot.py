from algo import get_words
import telebot
import database
from telebot import types

BOT_TOKEN = '6790284577:AAHb21_efi8q9JRoEIdI_ZeGVX48Og1Uyns'
signed_in = False
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    global signed_in
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    signed_in = False
    btn1 = types.KeyboardButton("Зарегистрироваться")
    btn2 = types.KeyboardButton("Авторизоваться")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Войдите в свою учётную запись или зарегистрируйте новую", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    global signed_in
    if(message.text == "Сгенерировать новую фразу" and signed_in == True):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сгенерировать новую фразу")
        btn2 = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, get_words(), reply_markup=markup)
    elif(message.text == "Зарегистрироваться" and signed_in == False):
        bot.send_message(message.chat.id, 'Введите имя')
        bot.register_next_step_handler(message, sign_up_name)
    elif(message.text == "Авторизоваться" and signed_in == False):
        bot.send_message(message.chat.id, 'Введите имя')
        bot.register_next_step_handler(message, sign_in_name)
    elif(signed_in == True):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сгенерировать новую фразу")
        btn2 = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2)
        text = 'Данный бот умеет генерировать случайные фразы. Для того чтобы бот сгенерировал новую фразу, нажмите на кнопку "Сгенерировать новую фразу".'
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зарегистрироваться")
        btn2 = types.KeyboardButton("Авторизоваться")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Войдите в свою учётную запись или зарегистрируйте новую", reply_markup=markup)

def sign_up_name(message):
    global name_sign_up
    name_sign_up = message.text
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, sign_up_password);
def sign_up_password(message):
    global password_sign_up
    password_sign_up = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Зарегистрироваться")
    btn2 = types.KeyboardButton("Авторизоваться")
    markup.add(btn1, btn2)
    try:
        database.insert(name_sign_up, password_sign_up)
    except Exception:
        bot.send_message(message.chat.id, "Пользователь с таким именем уже существует")
        bot.send_message(message.chat.id, "Войдите в свою учётную запись или зарегистрируйте новую", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Регистрация прошла успешно", reply_markup=markup)
def sign_in_name(message):
    global name_sign_in
    name_sign_in = message.text
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, sign_in_password);
def sign_in_password(message):
    global password_sign_in
    password_sign_in = message.text
    if database.check(name_sign_in, password_sign_in) == True:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сгенерировать новую фразу")
        btn2 = types.KeyboardButton("Помощь")
        global signed_in
        signed_in = True
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Здравствуйте, ' + name_sign_in + '!', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зарегистрироваться")
        btn2 = types.KeyboardButton("Авторизоваться")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Неверное имя или пароль', reply_markup=markup)
bot.infinity_polling()