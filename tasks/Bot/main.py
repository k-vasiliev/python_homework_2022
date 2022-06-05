#список нужных библиотек
from bot_config import get_token
import telebot
from telebot import types
import bot_text as bt
import emoji
import use_database as udb

#достанем токен и дадим его боту
token = get_token()
bot = telebot.TeleBot(token)

#задаем действия на команды
@bot.message_handler(commands=['start'])
def start(message, res=False):
    user_id = message.from_user.id
    if udb.db_select(f'select count(user_id) from users_data where user_id = {user_id}')[0] == 0:
        udb.db_insert('users_data', 'user_id', user_id)
        udb.db_insert('bot_questions', 'user_id', user_id)
        start_keys = types.InlineKeyboardMarkup()
        let_key = types.InlineKeyboardButton("Давай!", callback_data='Давай#123qq')
        start_keys.add(let_key)
        bot.send_message(message.chat.id, emoji.emojize(bt.start_text_newbie), reply_markup=start_keys)
    else:
        start_keys = types.InlineKeyboardMarkup()
        let_key = types.InlineKeyboardButton("Да, знакомы", callback_data='Знакомы#123qq')
        start_keys.add(let_key)
        bot.send_message(message.chat.id, emoji.emojize(bt.start_text_oldfag), reply_markup=start_keys)

@bot.message_handler(commands=['delete_user'])
def start(message, res=False):
    udb.delete_user(message.from_user.id)
    bot.send_message(message.chat.id, 'Пользователь удален')

#настраиваем сбор коллбэков с кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle(callback):
    #вытащим ИД пользователя
    user_id = callback.from_user.id
    #данные пользователя
    user_data = udb.db_select(f'select name, home_country, home_city from users_data where user_id = {user_id}')
    if callback.data == 'Давай#123qq':
        #справшиваем имя для знакомства
        bot.send_message(callback.message.chat.id, bt.ask_name)
        udb.db_update('bot_questions', 'name_q', 'name_q + 1', f'where user_id = {user_id}')
    #если знакомы, пробуем посмотреть, все ли заполнено
    if callback.data == 'Знакомы#123qq':
        unknown_data = 'Отлично, но я не знаю о тебе следующих вещей: \n'
        add_q_keys = types.InlineKeyboardMarkup()
        add_q_key = types.InlineKeyboardButton("Окей!", callback_data='Окей!#123qq')
        add_q_keys.add(add_q_key)
        if user_data != (None, None, None):
            bot.send_message(callback.message.chat.id, 'Прекрасно, рад твоему возвращению!')
        else:
            if user_data[0] is None:
                unknown_data += '-Твое имя\n'
            if user_data[1] is None:
                unknown_data += '-Твоя страна\n'
            if user_data[2] is None:
                unknown_data += '-Твой город\n'
            bot.send_message(callback.message.chat.id, unknown_data + '\n Давай их заполним?', reply_markup=add_q_keys)
    if callback.data == 'Окей!#123qq':

#настроим сборщик сообщений
@bot.message_handler(content_types=['text'])
def get_message(message):
    user_id = message.from_user.id  #вытащим ИД пользователя
    user_data = udb.db_select(f'select * from users_data where user_id = {user_id}')
    asked_q = user_data = udb.db_select(f'select * from bot_questions where user_id = {user_id}')

    #запишем имя в базу данных, игнорируем тот факт, что могут вотнуть всякую дичь
    # if bot_last_msg == bt.ask_name and user_data[1] is None:
    #     udb.db_update('users_data', 'name', message.text, f'where user_id = {user_id}')
    #     bot.send_message(message.chat.id, bt.ask_home_country)
    #     udb.db_update('bot_last_message', 'message_text', bt.ask_home_country, f'where user_id = {user_id}')
    # #запишем страну в базу данных
    # if bot_last_msg == bt.ask_home_country and user_data[2] is None:
    #     if udb.db_select(f'select count(distinct country) from geo where lower(country) = lower(trim(\'{message.text}\'))')[0] == 1:
    #         udb.db_update('users_data', 'home_country', message.text, f'where user_id = {user_id}')
    #         bot.send_message(message.chat.id, bt.ask_home_city)
    #         udb.db_update('bot_last_message', 'message_text', bt.ask_home_city, f'where user_id = {user_id}')
    #     else:
    #         bot.send_message(message.chat.id, emoji.emojize(bt.ask_again_home_country))
    # #запишем город в базу данных
    # if bot_last_msg == bt.ask_home_city and user_data[3] is None:
    #     if udb.db_select(f'select count(distinct city) from geo where lower(city) = lower(trim(\'{message.text}\'))')[0] == 1:
    #         udb.db_update('users_data', 'home_city', message.text, f'where user_id = {user_id}')
    #         bot.send_message(message.chat.id, bt.final_msg())
    #         udb.db_update('bot_last_message', 'message_text', bt.ask_home_city, f'where user_id = {user_id}')
    #     else:
    #         bot.send_message(message.chat.id, emoji.emojize(bt.ask_again_home_city))
    # else:
    #     bot.send_message(message.chat.id, 'Я тебя не понимаю')


bot.polling(none_stop=True, interval=0)
