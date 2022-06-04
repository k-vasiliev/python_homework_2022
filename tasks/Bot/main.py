#список нужных библиотек
from bot_config import get_token
import telebot
from telebot import types
import emoji
import sqlite3
import re
import requests


#достанем токен и дадим его боту
token = get_token()
bot = telebot.TeleBot(token)

#объявим базу-данных и все подключения
db_connection = sqlite3.connect('bot_database.db', check_same_thread=False)
db_cursor = db_connection.cursor()

#список дефолтных команд для бота и прочих переменных
start_text_newbie = str('Привет!:waving_hand: \n\n'
                        'Меня зовут Ботти и я бот-ежедневный помощник. я могу регулярно или по запросу, в удобное тебе время присылать следующий список нужной тебе информации: \n'
                        '-погода в твоем городе\n'
                        '-курс доллара и евро\n'
                        '-рандомную картинку\n'
                        '-установленное напоминание\n\n'
                        'Давай познакомимся?')

start_text_oldfag = str('Привет!:waving_hand: \n\n'
                        'Меня зовут Ботти и я бот-ежедневный помощник. я могу регулярно или по запросу, в удобное тебе время присылать следующий список нужной тебе информации: \n'
                        '-погода в твоем городе\n'
                        '-курс доллара и евро\n'
                        '-рандомную картинку\n'
                        '-установленное напоминание\n\n'
                        'Смотрю, мы уже знакомы?')

ask_name_text = str('Отлично! Напиши мне, как я могу к тебе обращаться?')

ask_home_country = str('Красивое имя! Из какой ты страны?')

#задаем текст на команду старт, вытягиваем ИД пользователя, чтобы сохранить его в БД, упоремся в простенький обработчик ошибок
@bot.message_handler(commands=['start'])
def start(message, res=False):
    try:
        user_id = message.from_user.id
        db_cursor.execute(f'insert into users_data(user_id) values ({user_id})') #создаем строку с пользователем в таблице с пользователями
        db_connection.commit()
        db_cursor.execute(f'insert into bot_last_message(user_id) values ({user_id})') #создаем строку с пользователем в таблице с последним сообщением
        db_connection.commit()
        start_keys = types.InlineKeyboardMarkup()
        let_key = types.InlineKeyboardButton("Давай!", callback_data='Давай#123qq')
        start_keys.add(let_key)
        bot.send_message(message.chat.id, emoji.emojize(start_text_newbie), reply_markup=start_keys)
        db_cursor.execute(f'update bot_last_message set message_text = \'{start_text_newbie}\' where user_id = {user_id}') #создаем строку с пользователем в таблице с последним сообщением
        db_connection.commit() #можно, конечно, решить словарем, но представим мы пишем бота для компании с 1000+ сотрудников и вечно падающим серваком
    #в базе user_id является уникальным ключ-значением, в случае, если инсертим такой же ID, то выдаст, что мы с ботом уже знакомы
    except:
        bot.send_message(message.chat.id, emoji.emojize(start_text_oldfag))

#настраиваем сбор коллбэков с кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle(callback):
    user_id = callback.from_user.id #вытащим ид пользователя
    if callback.data == 'Давай#123qq':
        bot.send_message(callback.message.chat.id, ask_name_text)
        db_cursor.execute(f'update bot_last_message set message_text = \'{ask_name_text}\' where user_id = {user_id}') #создаем строку с пользователем в таблице с последним сообщением
        db_connection.commit()

#настраиваем функцию сбор сообщений и обработчик на всякое разное
@bot.message_handler(content_types=['text'])
def get_message(message):
    user_id = message.from_user.id  # вытащим ид пользователя
    db_cursor.execute(f'select message_text from bot_last_message where user_id = {user_id}')
    #запишем имя в базу данных, игнорируем тот факт, что могут вотнуть всякую дичь
    if db_cursor.fetchone()[0] == ask_name_text:
        db_cursor.execute(f'update users_data set name = \'{message.text}\' where user_id = {user_id}') #создаем строку с пользователем в таблице с последним сообщением
        db_connection.commit()
        bot.send_message(message.chat.id, ask_home_country)
        db_cursor.execute(f'update bot_last_message set message_text = \'{ask_home_country}\' where user_id = {user_id}') #создаем строку с пользователем в таблице с последним сообщением
        db_connection.commit()



bot.polling(none_stop=True, interval=0)
