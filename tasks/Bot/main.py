#список нужных библиотек
from bot_config import get_token
import telebot
import emoji

#достанем токен
token = get_token()

bot = telebot.TeleBot(token)

#задаем текст на команду старт
@bot.message_handler(commands=['start'])
def start(message, res=False):
    bot.send_message(message.chat.id, emoji.emojize('Привет!:waving_hand: \n'
                                                    'Я - ежедневный помощник, я могу регулярно или по запросу, в удобное тебе время присылать следующий список нужной тебе информации: \n'
                                                    '-погода в твоем городе\n'
                                                    '-курс доллара и евро\n'
                                                    '-рандомную картинку\n'
                                                    '-установленное напоминание'))


@bot.message_handler(content_types=['text'])
def get_message(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True, interval=0)