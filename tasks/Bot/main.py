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

#поиграемся с функциями на ожидание ответа
def ask_name(message):
    name_keys = types.InlineKeyboardMarkup()
    name_keys.add(types.InlineKeyboardButton("И мне!", callback_data='И мне!#123qq'))
    user_id = message.from_user.id
    udb.db_update('users_data', 'name', '\'' + message.text + '\'', f'where user_id = {user_id}')
    msg = bot.send_message(message.chat.id, bt.greetings_msg(message.text), reply_markup=name_keys)

def ask_country(message):
    country_keys = types.InlineKeyboardMarkup()
    country_keys.add(types.InlineKeyboardButton("Тебе там понравится!", callback_data='Ттп#123qq'))
    user_id = message.from_user.id
    if udb.db_select(f'select count(distinct country) from geo where lower(country) = lower(trim(\'{message.text}\'))')[0] != 1:
        msg = bot.send_message(message.chat.id, emoji.emojize(bt.ask_again_home_country))
        bot.register_next_step_handler(msg, ask_country)
        return
    else:
        udb.db_update('users_data', 'home_country', '\'' + message.text + '\'', f'where user_id = {user_id}')
        msg = bot.send_message(message.chat.id, 'Круто, я бы очень хотел там побывать!', reply_markup=country_keys)

def ask_city(message):
    user_id = message.from_user.id
    if udb.db_select(f'select count(distinct city) from geo where lower(city) = lower(trim(\'{message.text}\'))')[0] != 1:
        msg = bot.send_message(message.chat.id, emoji.emojize(bt.ask_again_home_city))
        bot.register_next_step_handler(msg, ask_city)
        return
    else:
        udb.db_update('users_data', 'home_city', '\'' + message.text + '\'', f'where user_id = {user_id}')
        msg = bot.send_message(message.chat.id, 'Говорят, что это лучший город на свете!')

#задаем действия на команды
@bot.message_handler(commands=['start'])
def start(message, res=False):
    user_id = message.from_user.id
    if udb.db_select(f'select count(user_id) from users_data where user_id = {user_id}')[0] == 0:
        udb.db_insert('users_data', 'user_id', user_id)
        start_keys = types.InlineKeyboardMarkup()
        let_key = types.InlineKeyboardButton("Давай!", callback_data='Давай#123qq')
        start_keys.add(let_key)
        bot.send_message(message.chat.id, emoji.emojize(bt.start_text_newbie), reply_markup=start_keys)
    #обработчик на повторный старт
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
    if callback.data == 'Давай#123qq':
        #справшиваем имя для знакомства
        msg = bot.send_message(callback.message.chat.id, bt.ask_name)
        bot.register_next_step_handler(msg, ask_name)
    if callback.data == 'И мне!#123qq':
        msg = bot.send_message(callback.message.chat.id, bt.ask_home_country)
        bot.register_next_step_handler(msg, ask_country)
    if callback.data == 'Ттп#123qq':
        msg = bot.send_message(callback.message.chat.id, bt.ask_home_city)
        bot.register_next_step_handler(msg, ask_city)
    #если знакомы, пробуем посмотреть, все ли заполнено
    if callback.data == 'Знакомы#123qq':
        # данные пользователя
        user_data = udb.db_select(f'select name, home_country, home_city from users_data where user_id = {user_id}')
        unknown_data = 'Отлично, но я не знаю о тебе следующих вещей: \n'
        add_q_keys = types.InlineKeyboardMarkup()
        add_q_key = types.InlineKeyboardButton("Окей!", callback_data='Окей!#123qq')
        add_q_keys.add(add_q_key)
        if user_data != (None, None, None):
            bot.send_message(callback.message.chat.id, 'Прекрасно, рад твоему возвращению!')
        else:
            if user_data[0] is None:
                unknown_data += '-Твое имя\n'
            elif user_data[1] is None:
                unknown_data += '-Твоя страна\n'
            elif user_data[2] is None:
                unknown_data += '-Твой город\n'
            bot.send_message(callback.message.chat.id, unknown_data + '\n Давай их заполним?', reply_markup=add_q_keys)

#настроим сборщик сообщений
@bot.message_handler(content_types=['text'])
def get_message(message):
    user_id = message.from_user.id  #вытащим ИД пользователя
    user_data = udb.db_select(f'select * from users_data where user_id = {user_id}')



bot.polling(none_stop=True, interval=0)
