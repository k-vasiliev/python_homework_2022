#список нужных библиотек
import bot_func as bf
import telebot
from telebot import types
import bot_text as bt
import emoji
import use_database as udb

#достанем токены, зададим переменные для API
token = bf.get_token()
weather_token = bf.get_weather_token()

#запустим бота
bot = telebot.TeleBot(token)

#зададим клавиатуру
keyboard = types.ReplyKeyboardMarkup()
my_city_button = types.InlineKeyboardButton('В моем городе')
other_city_button = types.InlineKeyboardButton('Другой город')
geo_button = types.InlineKeyboardButton('По геолокации')
keyboard.row(my_city_button, other_city_button)
keyboard.row(geo_button)

#задаем действия на команды
#команда старт
@bot.message_handler(commands=['start'])
def start(message, res=False):
    user_id = message.from_user.id
    if udb.db_select(f'select count(user_id) from users_data where user_id = {user_id}')[0] == 0:
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

#команда на удаление пользователя из базы
@bot.message_handler(commands=['delete'])
def delete_user(message, res=False):
    udb.delete_user(message.from_user.id)
    bot.send_message(message.chat.id, 'Пользователь удален')

#команда для help
@bot.message_handler(commands=['help'])
def delete_user(message, res=False):
    bot.send_message(message.chat.id, bt.help)

#поиграемся с функциями на ожидание ответа
def ask_name(message):
    name_keys = types.InlineKeyboardMarkup()
    name_keys.add(types.InlineKeyboardButton("И мне!", callback_data='И мне!#123qq'))
    user_id = message.from_user.id
    if message.text.lower() == '/delete':
        udb.delete_user(message.from_user.id)
        bot.send_message(message.chat.id, 'Пользователь удален')
    elif message.text.find('/') > -1:
        msg = bot.send_message(message.chat.id, emoji.emojize(bt.wrong_name))
        bot.register_next_step_handler(msg, ask_name)
    else:
        udb.db_insert('users_data', 'user_id', user_id) #вставим нового пользователя
        udb.db_update('users_data', 'name', '\'' + message.text + '\'', f'where user_id = {user_id}')
        bot.send_message(message.chat.id, bt.greetings_msg(message.text), reply_markup=name_keys)

def ask_country(message):
    country_keys = types.InlineKeyboardMarkup()
    country_keys.add(types.InlineKeyboardButton("Тебе там понравится!", callback_data='Ттп#123qq'))
    user_id = message.from_user.id
    if message.text.lower() == '/delete':
        udb.delete_user(message.from_user.id)
        bot.send_message(message.chat.id, 'Пользователь удален')
    elif udb.db_select(f'select count(distinct country) from geo where lower(country) = lower(trim(\'{message.text}\'))')[0] == 0:
        msg = bot.send_message(message.chat.id, emoji.emojize(bt.ask_again_home_country))
        bot.register_next_step_handler(msg, ask_country)
    else:
        udb.db_update('users_data', 'home_country', '\'' + message.text + '\'', f'where user_id = {user_id}')
        bot.send_message(message.chat.id, 'Круто, я бы очень хотел там побывать!', reply_markup=country_keys)

def ask_city(message):
    user_id = message.from_user.id
    if message.text.lower() == '/delete':
        udb.delete_user(message.from_user.id)
        bot.send_message(message.chat.id, 'Пользователь удален')
    elif udb.db_select(f'select count(distinct city) from geo where lower(city) = lower(trim(\'{message.text}\'))')[0] == 0:
        msg = bot.send_message(message.chat.id, emoji.emojize(bt.ask_again_home_city))
        bot.register_next_step_handler(msg, ask_city)
    else:
        udb.db_update('users_data', 'home_city', '\'' + message.text + '\'', f'where user_id = {user_id}')
        bot.send_message(message.chat.id, bt.final, reply_markup=keyboard)

def ask_city_forecast(message):
    location_msg = message.text.replace(' ', '').split(',')
    location_geo = udb.db_select(f'select lat, lng from geo where lower(country) = lower(\'{location_msg[0]}\') and lower(city) = lower(\'{location_msg[1]}\')')
    if location_geo[0] is None:
        msg = bot.send_message(message.chat.id, 'Я не нашел такого города, попробуй еще раз')
        bot.register_next_step_handler(msg, ask_city_forecast)
    else:
        user_id = message.from_user.id  # вытащим ИД пользователя
        user_data = udb.db_select(f'select name, home_country, home_city from users_data where user_id = {user_id}')  # данные пользователя
        lat = location_geo[0]
        lon = location_geo[1]
        location = bf.get_location_data(weather_token, lat, lon)
        forecast = bf.get_forecast(weather_token, location[0])
        bot.send_message(message.chat.id, f'{user_data[0]}, вот погода в {location[1]}, {location[2]}:\n\n' + forecast)

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
        if user_data is None:
            msg = bot.send_message(callback.message.chat.id, bt.ask_name_break)
            bot.register_next_step_handler(msg, ask_name)
        elif sum(x is not None for x in user_data) == 3:
            bot.send_message(callback.message.chat.id, 'Прекрасно, рад твоему возвращению!')
        else:
            if user_data[0] is None:
                msg = bot.send_message(callback.message.chat.id, bt.ask_name_break)
                bot.register_next_step_handler(msg, ask_name)
            elif user_data[1] is None:
                msg = bot.send_message(callback.message.chat.id, bt.ask_home_country_break)
                bot.register_next_step_handler(msg, ask_country)
            elif user_data[2] is None:
                msg = bot.send_message(callback.message.chat.id, bt.ask_home_city_break)
                bot.register_next_step_handler(msg, ask_city)


#настроим сборщик сообщений
@bot.message_handler(content_types=['text'])
def get_message(message):
    user_id = message.from_user.id  #вытащим ИД пользователя
    user_data = udb.db_select(f'select name, home_country, home_city from users_data where user_id = {user_id}') #данные пользователя
    if user_data is None:
        msg = bot.send_message(message.chat.id, bt.ask_name_break)
        bot.register_next_step_handler(msg, ask_name)
    elif sum(x is not None for x in user_data) != 3:
        if user_data[0] is None:
            msg = bot.send_message(message.chat.id, bt.ask_name_break)
            bot.register_next_step_handler(msg, ask_name)
        elif user_data[1] is None:
            msg = bot.send_message(message.chat.id, bt.ask_home_country_break)
            bot.register_next_step_handler(msg, ask_country)
        elif user_data[2] is None:
            msg = bot.send_message(message.chat.id, bt.ask_home_city_break)
            bot.register_next_step_handler(msg, ask_city)
    elif message.text.lower().strip() == 'в моем городе':
        user_home_geo = udb.db_select(f'select lat, lng from geo where country = \'{user_data[1]}\' and city = \'{user_data[2]}\'')
        location = bf.get_location_data(weather_token, user_home_geo[0], user_home_geo[1])
        forecast = bf.get_forecast(weather_token, location[0])
        bot.send_message(message.chat.id, f'{user_data[0]}, вот погода в {location[1]}, {location[2]}:\n\n' + forecast, reply_markup=keyboard)
    elif message.text.lower().strip() == 'другой город':
        msg = bot.send_message(message.chat.id, 'Пришли мне страну и город через запятую, например: Россия, Тверь')
        bot.register_next_step_handler(msg, ask_city_forecast)
    elif message.text.lower().strip() == 'по геолокации':
        bot.send_message(message.chat.id, 'Пришли мне свою гелокацию')
    else:
        bot.send_message(message.chat.id, bt.use_keyboard, reply_markup=keyboard)

#по гелокации
@bot.message_handler(content_types=['location'])
def handle_location(message):
    user_id = message.from_user.id  #вытащим ИД пользователя
    user_data = udb.db_select(f'select name, home_country, home_city from users_data where user_id = {user_id}') #данные пользователя
    lat = message.location.latitude
    lon = message.location.longitude
    location = bf.get_location_data(weather_token, lat, lon)
    forecast = bf.get_forecast(weather_token, location[0])
    bot.send_message(message.chat.id, f'{user_data[0]}, вот погода в {location[1]}, {location[2]}:\n\n' + forecast, reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)
