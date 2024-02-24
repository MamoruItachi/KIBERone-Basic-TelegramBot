import telebot
import openpyxl
from telebot import types
import random
from random import choice

book = openpyxl.open("ivent.xlsx",read_only=True)
sheet = book.active

bot = telebot.TeleBot('6846423247:AAHSK5YeYZ-0x1BB67CUuF3evMVDKnjQaO8')

itfacts = ['В Гималаях (юго-западный Китай) живет малая панда (красная панда). В английском языке её называют «Firefox». Это слово вдохновило создателей популярного браузера… вот только на логотип они почему-то поместили красную лису, а не панду.', 'На самом первом логотипе Apple был изображен сидящий под яблоней сэр Исаак Ньютон. Над ним нависает вот-вот готовое упасть яблоко.', 'Компакт-диски (CD) читаются от внутреннего круга до наружного, а записываются с точностью до наоборот.', 'Среднестатистический пользователь компьютера моргает 7 раз в минуту. Нормальный показатель – 12 раз в минуту.', 'Пальцы наборщика текста в среднем за день «пробегают» 20 км.', 'Первый в мире будильник умел звонить только в 4 часа утра.', '30 ноября каждого года отмечается Всемирный день компьютерной безопасности («Computer Security Day“)', 'Радио потребовалось 38 лет, чтобы набрать рыночную аудиторию в 50 млн слушателей, телевидению — 13 лет, iPod — 3 года.', 'Снимок, сделанный самой первой фотокамерой в мире, пришлось бы ждать 8 часов.', 'Skype официально заблокирован в Китае.', 'Текст с экрана читается на 10% медленнее, чем с бумаги.', 'Название популярного Linux-дистрибутива Ubuntu взято из одного из африканских языков. Оно означает «Я из-за тебя».',]

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Информация')
    btn2 = types.KeyboardButton('Ученики')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Тестовы бот для KIBERone/Описание измениться", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    #Информация
    if message.text == 'Информация':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💳 Оплата')
        btn2 = types.KeyboardButton('👩🏻‍🏫 Тьюторы')
        btn3 = types.KeyboardButton('🎬 Социальные-Медиа')
        btn4 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn5 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, "👋 Информация о школе KIBERone", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    elif message.text == '🔙 Вернуться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Информация')
        btn2 = types.KeyboardButton('Ученики')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Тестовы бот для KIBERone/Описание измениться", reply_markup=markup)

    #Рандомные факты
    elif message.text == '👀 Ты этого точно не знал!':
        for i in range(1):
            bot.send_message(message.from_user.id, random.choice(itfacts))

    #ОПЛАТА
    elif message.text == '💳 Оплата':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тест оплата', reply_markup=markup, parse_mode='Markdown')

    #ТЬЮТОРЫ
    elif message.text == '👩🏻‍🏫 Тьюторы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Список тьюторов', reply_markup=markup, parse_mode='Markdown')

    #СОЦИАЛЬНЫЕ МЕДИА
    elif message.text == '🎬 Социальные-Медиа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('📷 Вк')
        markup.add(btn01, btn1)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    #ВЫХОД В ГЛАВНОЕ МЕНЮ
    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💳 Оплата')
        btn2 = types.KeyboardButton('👩🏻‍🏫 Тьюторы')
        btn3 = types.KeyboardButton('🎬 Социальные-Медиа')
        btn4 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn5 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, "👋 Информация о школе KIBERone", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')



    #Ученики
    elif message.text == 'Ученики':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📅 Расписание')
        btn2 = types.KeyboardButton('📁 Проекты и мероприятия')
        btn3 = types.KeyboardButton('📚 Знания')
        btn4 = types.KeyboardButton('💻 Навигация профессий')
        btn5 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn6 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, "👋 Информация о резиденте KIBERone", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
    
    elif message.text == '🔙 Вернуться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Информация')
        btn2 = types.KeyboardButton('Ученики')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Тестовы бот для KIBERone/Описание измениться", reply_markup=markup)

    #РАСПИСАНИЕ
    elif message.text == '📅 Расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть расписание', reply_markup=markup, parse_mode='Markdown')

    #ПРОЕКТЫ И МЕРОПРИЯТИЯ
    elif message.text == '📁 Проекты и мероприятия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('🔎 Олимпиада KIBERone - Scratch')
        btn2 = types.KeyboardButton('🔎 Олимпиада KIBERone - Kodu Game Lab')
        btn3 = types.KeyboardButton('🔎 Олимпиада KIBERone - Roblox Studio')
        btn4 = types.KeyboardButton('🔎 Хакатон KIBERone')
        btn5 = types.KeyboardButton('🔎 Скоро будут')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🔎 Олимпиада KIBERone - Scratch':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('🔎 Олимпиада KIBERone - Scratch')
        btn2 = types.KeyboardButton('🔎 Олимпиада KIBERone - Kodu Game Lab')
        btn3 = types.KeyboardButton('🔎 Олимпиада KIBERone - Roblox Studio')
        btn4 = types.KeyboardButton('🔎 Хакатон KIBERone')
        btn5 = types.KeyboardButton('🔎 Скоро будут')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, sheet["A2"].value, reply_markup=markup)

    elif message.text == '🔎 Олимпиада KIBERone - Kodu Game Lab':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('🔎 Олимпиада KIBERone - Scratch')
        btn2 = types.KeyboardButton('🔎 Олимпиада KIBERone - Kodu Game Lab')
        btn3 = types.KeyboardButton('🔎 Олимпиада KIBERone - Roblox Studio')
        btn4 = types.KeyboardButton('🔎 Хакатон KIBERone')
        btn5 = types.KeyboardButton('🔎 Скоро будут')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, sheet["B2"].value, reply_markup=markup)
        
    
    elif message.text == '🔎 Олимпиада KIBERone - Roblox Studio':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('🔎 Олимпиада KIBERone - Scratch')
        btn2 = types.KeyboardButton('🔎 Олимпиада KIBERone - Kodu Game Lab')
        btn3 = types.KeyboardButton('🔎 Олимпиада KIBERone - Roblox Studio')
        btn4 = types.KeyboardButton('🔎 Хакатон KIBERone')
        btn5 = types.KeyboardButton('🔎 Скоро будут')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, sheet["C2"].value, reply_markup=markup)
         
    
    elif message.text == '🔎 Хакатон KIBERone':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('🔎 Олимпиада KIBERone - Scratch')
        btn2 = types.KeyboardButton('🔎 Олимпиада KIBERone - Kodu Game Lab')
        btn3 = types.KeyboardButton('🔎 Олимпиада KIBERone - Roblox Studio')
        btn4 = types.KeyboardButton('🔎 Хакатон KIBERone')
        btn5 = types.KeyboardButton('🔎 Скоро будут')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, sheet["D2"].value, reply_markup=markup)
        

    elif message.text == '🔎 Скоро будут':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('🔎 Олимпиада KIBERone - Scratch')
        btn2 = types.KeyboardButton('🔎 Олимпиада KIBERone - Kodu Game Lab')
        btn3 = types.KeyboardButton('🔎 Олимпиада KIBERone - Roblox Studio')
        btn4 = types.KeyboardButton('🔎 Хакатон KIBERone')
        btn5 = types.KeyboardButton('🔎 Скоро будут')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, sheet["E2"].value, reply_markup=markup)
        

    #ЗНАНИЯ
    elif message.text == '📚 Знания':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('📚 Книги')
        btn2 = types.KeyboardButton('📚 Фильмы')
        markup.add(btn01, btn1, btn2)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)
    
    elif message.text == '📚 Книги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Список книг', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Фильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Список фильмов', reply_markup=markup, parse_mode='Markdown')

    #НАВИГАЦИЯ ПРОФЕССИЙ
    elif message.text == '💻 Навигация профессий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton("🛠 Frontend-developer")
        btn2 = types.KeyboardButton('🛠 Backend-developer')
        btn3 = types.KeyboardButton('🛠 Game-developer')
        btn4 = types.KeyboardButton('🛠 Тестировщик')
        btn5 = types.KeyboardButton('🛠 Разработчик искусственного интеллекта')
        btn6 = types.KeyboardButton('🛠 3d художник')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🛠 Frontend-developer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '🛠 Backend-developer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🛠 Game-developer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '🛠 Тестировщик':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '🛠 Разработчик искусственного интеллекта':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🛠 3d художник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')

    #ГЛАВНОЕ МЕНЮ УЧЕНИКА
    elif message.text == '🔙 Главное меню ученика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📅 Расписание')
        btn2 = types.KeyboardButton('📁 Проекты и мероприятия')
        btn3 = types.KeyboardButton('📚 Знания')
        btn4 = types.KeyboardButton('💻 Навигация профессий')
        btn5 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn6 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, "👋 Информация о резиденте KIBERone", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
    

bot.polling(none_stop=True, interval=0) 