"""

"""
from dataclasses import dataclass
from random import choice

import telebot
from telebot import types

bot = telebot.TeleBot('6949937561:AAEsEhaQE6spVOyzJo_ogxMExjrT5Kywefk')

itfacts = (
    'В Гималаях (юго-западный Китай) живет малая панда (красная панда). В английском языке её называют «Firefox». Это слово вдохновило создателей популярного браузера… вот только на логотип они почему-то поместили красную лису, а не панду.',
    'На самом первом логотипе Apple был изображен сидящий под яблоней сэр Исаак Ньютон. Над ним нависает вот-вот готовое упасть яблоко.',
    'Компакт-диски (CD) читаются от внутреннего круга до наружного, а записываются с точностью до наоборот.',
    'Среднестатистический пользователь компьютера моргает 7 раз в минуту. Нормальный показатель – 12 раз в минуту.',
    'Пальцы наборщика текста в среднем за день «пробегают» 20 км.',
    'Первый в мире будильник умел звонить только в 4 часа утра.',
    '30 ноября каждого года отмечается Всемирный день компьютерной безопасности («Computer Security Day“)',
    'Радио потребовалось 38 лет, чтобы набрать рыночную аудиторию в 50 млн слушателей, телевидению — 13 лет, iPod — 3 года.',
    'Снимок, сделанный самой первой фотокамерой в мире, пришлось бы ждать 8 часов.',
    'Skype официально заблокирован в Китае.', 'Текст с экрана читается на 10% медленнее, чем с бумаги.',
    'Название популярного Linux-дистрибутива Ubuntu взято из одного из африканских языков. Оно означает «Я из-за тебя».',)


@dataclass
class ButtonLabel:
    BUTTON_INFORMATION = 'Информация'
    BUTTON_STUDENTS = 'Ученики'
    BUTTON_PAYMENT = '💳 Оплата'
    BUTTON_TUTOR = '👩🏻‍🏫 Тьюторы'
    BUTTON_SOCIAL_MEDIA = '🎬 Социальные-Медиа'
    BUTTON_INTERESTING_FACT = '👀 Ты этого точно не знал!'
    BUTTON_BACK = '🔙 Вернуться'
    BUTTON_MAIN_MENU = '🔙 Главное меню'
    BUTTON_SCHEDULE = '📅 Расписание'
    BUTTON_PROJECTS_EVENTS = '📁 Проекты и мероприятия'
    BUTTON_USEFUL_SOURCES = '📚 Знания'
    BUTTON_PROFESSION_NAVIGATION = '💻 Навигация профессий'
    BUTTON_STUDENT_MENU = '🔙 Главное меню ученика'

    @staticmethod
    def get_button_label_main_menu():
        return (
            ButtonLabel.BUTTON_INFORMATION,
            ButtonLabel.BUTTON_STUDENTS
        )

    @staticmethod
    def get_button_label_information_menu():
        return (
            ButtonLabel.BUTTON_PAYMENT,
            ButtonLabel.BUTTON_TUTOR,
            ButtonLabel.BUTTON_SOCIAL_MEDIA,
            ButtonLabel.BUTTON_INTERESTING_FACT,
            ButtonLabel.BUTTON_BACK
        )

    @staticmethod
    def get_button_label_students_menu():
        return (
            ButtonLabel.BUTTON_SCHEDULE,
            ButtonLabel.BUTTON_PROJECTS_EVENTS,
            ButtonLabel.BUTTON_USEFUL_SOURCES,
            ButtonLabel.BUTTON_PROFESSION_NAVIGATION,
            ButtonLabel.BUTTON_INTERESTING_FACT,
            ButtonLabel.BUTTON_BACK
        )


class Settings:
    scene_changed = True
    current_scene_index = '/start'
    last_scene_index = []

    @staticmethod
    def set_scene(index):
        Settings.scene_changed = True
        Settings.current_scene_index = index
        if index not in Settings.last_scene_index:
            Settings.last_scene_index.append(index)

    @staticmethod
    def set_back_scene():
        if len(Settings.last_scene_index) > 1:
            Settings.last_scene_index.pop()
            Settings.set_scene(Settings.last_scene_index[-1])


class BaseScene:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.button_labels: tuple[str] = ()
        self.texts_message: list[str] = []

    def activate(self, message: telebot.types.Message):
        self.generate_markup()
        self.send_message(message)

    def event(self, text):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Settings.scene_changed = False
        if text in SCENES_TRIGGER.keys():
            Settings.set_scene(SCENES_TRIGGER[text].SCENE_INDEX)
        if text == ButtonLabel.BUTTON_BACK:
            Settings.set_back_scene()
        self.additional_event(text)

    def additional_event(self, text):
        # TODO document why this method is empty
        pass

    def generate_markup(self) -> object:
        self.markup.add(*self.button_labels)
        # for label in self.button_labels:
        #     self.markup.add(label)
        self.additional_button()

    def additional_button(self) -> object:
        # TODO documents
        pass

    def send_message(self, message: telebot.types.Message) -> object:
        for text in self.texts_message:
            bot.send_message(message.chat.id, text=text, reply_markup=self.markup)


class StartScene(BaseScene):
    SCENE_INDEX = '/start'

    def __init__(self):
        super().__init__()
        self.texts_message.append("Тестовый бот для KIBERone/Описание измениться")
        self.button_labels = ButtonLabel.get_button_label_main_menu()


class InformationScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_INFORMATION

    def __init__(self):
        super().__init__()
        self.button_labels = ButtonLabel.get_button_label_information_menu()
        self.texts_message = ["👋 Информация о школе KIBERone", '👀 Выберите интересующий вас раздел']


class StudentsScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_STUDENTS

    def __init__(self):
        super().__init__()
        self.button_labels = ButtonLabel.get_button_label_students_menu()
        self.texts_message = ["👋 Информация о школе KIBERone", '👀 Выберите интересующий вас раздел']


class PaymentScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_PAYMENT

    def __init__(self):
        super().__init__()


class TutorScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_TUTOR

    def __init__(self):
        super().__init__()


class SocialMediaScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_SOCIAL_MEDIA

    def __init__(self):
        super().__init__()


class InterestingFactScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_INTERESTING_FACT

    def __init__(self):
        super().__init__()


class ScheduleScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_SCHEDULE

    def __init__(self):
        super().__init__()


class ProjectsEventsScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_PROJECTS_EVENTS

    def __init__(self):
        super().__init__()


class UsefulSourcesScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_USEFUL_SOURCES

    def __init__(self):
        super().__init__()


class ProfessionNavigationScene(BaseScene):
    SCENE_INDEX = ButtonLabel.BUTTON_PROFESSION_NAVIGATION

    def __init__(self):
        super().__init__()


SCENES_TRIGGER = {
    '/start': StartScene(),
    ButtonLabel.BUTTON_INFORMATION: InformationScene(),
    ButtonLabel.BUTTON_STUDENTS: StudentsScene(),
    ButtonLabel.BUTTON_PAYMENT: PaymentScene(),
    ButtonLabel.BUTTON_TUTOR: TutorScene(),
    ButtonLabel.BUTTON_SOCIAL_MEDIA: SocialMediaScene(),
    ButtonLabel.BUTTON_SCHEDULE: ScheduleScene(),
    ButtonLabel.BUTTON_PROJECTS_EVENTS: ProjectsEventsScene(),
    ButtonLabel.BUTTON_USEFUL_SOURCES: UsefulSourcesScene(),
    ButtonLabel.BUTTON_PROFESSION_NAVIGATION: ProfessionNavigationScene(),
}


class Application:
    def __init__(self):
        # TODO document why this method is empty
        self.scene = None
        pass

    def find_cur_scene(self):
        for val in SCENES_TRIGGER.values():
            if val.SCENE_INDEX == Settings.current_scene_index:
                self.scene = val

    def run(self, message: telebot.types.Message):
        try:
            SCENES_TRIGGER[Settings.current_scene_index].event(message.text)
            if Settings.scene_changed:
                SCENES_TRIGGER[Settings.current_scene_index].activate(message)
        except TypeError:
            print(message)


# @bot.message_handler(commands=['start'])  # стартовая команда
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton('Информация')
#     btn2 = types.KeyboardButton('Ученики')
#     markup.add(btn1, btn2)
#     bot.send_message(message.from_user.id, "Тестовый бот для KIBERone/Описание измениться", reply_markup=markup)
#

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    app = Application()
    app.run(message)
    # Информация
    # print(type(message))
    # if message.text == 'Информация':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('💳 Оплата')
    #     btn2 = types.KeyboardButton('👩🏻‍🏫 Тьюторы')
    #     btn3 = types.KeyboardButton('🎬 Социальные-Медиа')
    #     btn4 = types.KeyboardButton('👀 Ты этого точно не знал!')
    #     btn5 = types.KeyboardButton('🔙 Вернуться')
    #     markup.add(btn1, btn2, btn3, btn4, btn5)
    #     bot.send_message(message.from_user.id, "👋 Информация о школе KIBERone", reply_markup=markup)
    #     bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
    #
    # elif message.text == '🔙 Вернуться':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('Информация')
    #     btn2 = types.KeyboardButton('Ученики')
    #     markup.add(btn1, btn2)
    #     bot.send_message(message.from_user.id, "Тестовы бот для KIBERone/Описание измениться", reply_markup=markup)
    #
    # # Рандомные факты
    # elif message.text == '👀 Ты этого точно не знал!':
    #     for _ in range(1):
    #         bot.send_message(message.from_user.id, choice(itfacts))
    #
    # # ОПЛАТА
    # elif message.text == '💳 Оплата':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Тест оплата', reply_markup=markup, parse_mode='Markdown')
    #
    # # ТЬЮТОРЫ
    # elif message.text == '👩🏻‍🏫 Тьюторы':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Список тьюторов', reply_markup=markup, parse_mode='Markdown')
    #
    # # СОЦИАЛЬНЫЕ МЕДИА
    # elif message.text == '🎬 Социальные-Медиа':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn01 = types.KeyboardButton('🔙 Главное меню')
    #     btn1 = types.KeyboardButton('📷 Вк')
    #     markup.add(btn01, btn1)
    #     bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)
    #
    # # ВЫХОД В ГЛАВНОЕ МЕНЮ
    # elif message.text == '🔙 Главное меню':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('💳 Оплата')
    #     btn2 = types.KeyboardButton('👩🏻‍🏫 Тьюторы')
    #     btn3 = types.KeyboardButton('🎬 Социальные-Медиа')
    #     btn4 = types.KeyboardButton('👀 Ты этого точно не знал!')
    #     btn5 = types.KeyboardButton('🔙 Вернуться')
    #     markup.add(btn1, btn2, btn3, btn4, btn5)
    #     bot.send_message(message.from_user.id, "👋 Информация о школе KIBERone", reply_markup=markup)
    #     bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
    #
    # # Ученики
    # elif message.text == 'Ученики':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('📅 Расписание')
    #     btn2 = types.KeyboardButton('📁 Проекты и мероприятия')
    #     btn3 = types.KeyboardButton('📚 Знания')
    #     btn4 = types.KeyboardButton('💻 Навигация профессий')
    #     btn5 = types.KeyboardButton('👀 Ты этого точно не знал!')
    #     btn6 = types.KeyboardButton('🔙 Вернуться')
    #     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    #     bot.send_message(message.from_user.id, "👋 Информация о резиденте KIBERone", reply_markup=markup)
    #     bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
    #
    # elif message.text == '🔙 Вернуться':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('Информация')
    #     btn2 = types.KeyboardButton('Ученики')
    #     markup.add(btn1, btn2)
    #     bot.send_message(message.from_user.id, "Тестовы бот для KIBERone/Описание измениться", reply_markup=markup)
    #
    # # РАСПИСАНИЕ
    # elif message.text == '📅 Расписание':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Тут должно быть расписание', reply_markup=markup, parse_mode='Markdown')
    #
    # # ПРОЕКТЫ И МЕРОПРИЯТИЯ
    # elif message.text == '📁 Проекты и мероприятия':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn01 = types.KeyboardButton('🔙 Главное меню ученика')
    #     btn1 = types.KeyboardButton('🔎 Олимпиада KIBERone - Scratch')
    #     btn2 = types.KeyboardButton('🔎 Олимпиада KIBERone - Kodu Game Lab')
    #     btn3 = types.KeyboardButton('🔎 Олимпиада KIBERone - Roblox Studio')
    #     btn4 = types.KeyboardButton('🔎 Скоро будут')
    #     markup.add(btn01, btn1, btn2, btn3, btn4, btn4)
    #     bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)
    #
    # # ЗНАНИЯ
    # elif message.text == '📚 Знания':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn01 = types.KeyboardButton('🔙 Главное меню ученика')
    #     btn1 = types.KeyboardButton('📚 Книги')
    #     btn2 = types.KeyboardButton('📚 Фильмы')
    #     markup.add(btn01, btn1, btn2)
    #     bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)
    #
    # elif message.text == '📚 Книги':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Список книг', reply_markup=markup, parse_mode='Markdown')
    #
    # elif message.text == '📚 Фильмы':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Список фильмов', reply_markup=markup, parse_mode='Markdown')
    #
    # # НАВИГАЦИЯ ПРОФЕССИЙ
    # elif message.text == '💻 Навигация профессий':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn01 = types.KeyboardButton('🔙 Главное меню ученика')
    #     btn1 = types.KeyboardButton("🛠 Frontend-developer")
    #     btn2 = types.KeyboardButton('🛠 Backend-developer')
    #     btn3 = types.KeyboardButton('🛠 Game-developer')
    #     btn4 = types.KeyboardButton('🛠 Тестировщик')
    #     btn5 = types.KeyboardButton('🛠 Разработчик искусственного интеллекта')
    #     btn6 = types.KeyboardButton('🛠 3d художник')
    #     markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6)
    #     bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)
    #
    # elif message.text == '🛠 Frontend-developer':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    #
    # elif message.text == '🛠 Backend-developer':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    #
    # elif message.text == '🛠 Game-developer':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    #
    # elif message.text == '🛠 Тестировщик':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    #
    # elif message.text == '🛠 Разработчик искусственного интеллекта':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    #
    # elif message.text == '🛠 3d художник':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('🔙 Главное меню ученика')
    #     markup.add(btn1)
    #     bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    #
    # # ГЛАВНОЕ МЕНЮ УЧЕНИКА
    # elif message.text == '🔙 Главное меню ученика':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton('📅 Расписание')
    #     btn2 = types.KeyboardButton('📁 Проекты и мероприятия')
    #     btn3 = types.KeyboardButton('📚 Знания')
    #     btn4 = types.KeyboardButton('💻 Навигация профессий')
    #     btn5 = types.KeyboardButton('👀 Ты этого точно не знал!')
    #     btn6 = types.KeyboardButton('🔙 Вернуться')
    #     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    #     bot.send_message(message.from_user.id, "👋 Информация о резиденте KIBERone", reply_markup=markup)
    #     bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')


bot.polling(none_stop=True, interval=0)
