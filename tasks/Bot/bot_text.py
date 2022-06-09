#список длинных фраз, которые может отправить бот, либо обернутые в функции фразы
start_text_newbie = str('Привет!:waving_hand: \n\n'
                        'Я очередной погодный бот, которых великое множество.\n'
                        'А еще я немного душный "товарищ майор", который не даст тебе узнать погоду, пока мы не познакомимся.\n'
                        'Назови, пожалуйста, мне свое имя, чтобы я знал как к тебе обращаться, страну и город.\n'
                        'Эти данные помогут мне отсылать тебе погоду по одному нажатию кнопки.\n'
                        'Ну что, давай познакомимся?')

start_text_oldfag = str('Привет!:waving_hand: \n\n'
                        'Я очередной погодный бот, которых великое множествою\n'
                        'А еще я немного душный "товарищ майор", который не даст тебе узнать погоду, пока мы не познакомимся.\n'
                        'Назови, пожалуйста, мне свое имя, чтобы я знал как к тебе обращаться, страну и город.\n'
                        'Эти данные помогут мне отсылать тебе погоду по одному нажатию кнопки.\n'
                        'Вижу, ты уже заходил ко мне и мы немного знакомы?')

ask_name = 'Отлично! Напиши мне, как я могу к тебе обращаться?'
wrong_name = 'В имени не может быть символа /, введи, пожалуйста, правильно свое имя:)'
ask_name_break = 'Рад тебя видеть! В прошлый раз ты не указал свое имя, как я могу к тебе обращаться?'

ask_home_country = 'Красивое имя! Из какой ты страны?'
ask_home_country_break = 'Напомни, в какой стране ты живешь?'
ask_again_home_country = 'Я не знаю такой страны :disappointed_face:. Попробуй ввести еще раз.'

ask_home_city = 'А в каком городе ты живешь?'
ask_home_city_break = 'Уточни, из какого ты города?'
ask_again_home_city = 'Я не знаю такого города :disappointed_face:. Попробуй ввести еще раз.'

final = 'Говорят, что это лучший город на свете!\n Ну вот и все, мы познакомились, открывай клавиатуру и нажимай специальные кнопочки!'

help = str('Я погодный бот, который умеет присылать тебе погоду (спасибо, Адмирал Ясен Буй)\n'
            'Команды для работы со мной:\n'
            '/start - чтобы начать знакомство \n'
            '/help - вызвать эту же подсказку \n'
            '/delete - удалить себя, для любителей теории заговора\n\n'      
            'Для всего остального используй встроенную клавиатуру')

use_keyboard = 'Для удобства используй специальную клавиатуру для запроса погоды:)'

def greetings_msg(name):
    return f'Приятно познакомиться, {name}!'

def final_msg(name, city):
    return f'Приятно познакомиться, {name} из города {city}!'