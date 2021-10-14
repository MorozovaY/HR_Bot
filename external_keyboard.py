from telegram import ReplyKeyboardMarkup
from handlers import main_keyboard

def external_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Про компанию', 'Наши офисы'],
            ['Карьера в компании', 'Подписаться на новости'],
            ['Вернуться в главное меню']
        ])


def company_external(update, context):
    update.message.reply_text(
        'Здесь будет более расширенная информация о компании',
        reply_markup=external_keyboard()
    )


def offices_external(update, context):
    update.message.reply_text(
        'Здесь будет более расширенная информация про офисы и филиалы',
        reply_markup=external_keyboard()
    )


def career(update, context):
    update.message.reply_text(
        'Здесь должны быть ссылки на хх компании и возможность отправить резюме',
        reply_markup=external_keyboard()
    )


def news(update, context):
    update.message.reply_text(
        'Если человек нажал кнопку, присылать автоматически новые статьи с хабра компании',
        reply_markup=external_keyboard()
    )

def back(update, context):
    update.message.reply_text(
        'Добро пожаловать в главное меню',
        reply_markup=main_keyboard()
    )
