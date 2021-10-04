from telegram import ReplyKeyboardRemove
from telegram.ext import  ConversationHandler
from handlers import main_keyboard

from db import db_session
from db import User

def anketa_start(update, context):
    context.user_data['anketa'] = dict()
    update.message.reply_text(
        'Вы перешли в раздел регистрация.'
        'Пожалуйста, введите, как Вас зовут через пробел в формате: ФАМИЛИЯ ИМЯ ОТЧЕСТВО',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'


def anketa_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 3:
        update.message.reply_text('Пожалуйста, введите фамилию, имя и отчество')
        return 'name'
    else:
        context.user_data['anketa']['name'] = update.message.text
        update.message.reply_text(
            'Введите город проживания'
        )
        return 'city'


def anketa_city(update, context):
    context.user_data['anketa']['city'] = update.message.text
    update.message.reply_text('Введите телефон для связи')
    return 'phone'


def anketa_phone(update, context):
    context.user_data['anketa']['phone'] = update.message.text
    update.message.reply_text(
        'Вы можете прикрепить Ваше резюме файлом в формате .pdf '
        'Либо можете пропустить этот этап нажав /skip'
    )
    return 'cv'


def anketa_cv(update, context):
    context.user_data['anketa']['cv'] = update.message.text
    update.message.reply_text(
        'Регистрация завершена.',
        reply_markup=main_keyboard()
    )
    anketa_data = context.user_data.get('anketa', 'None')
    name = anketa_data['name']
    city = anketa_data['city']
    phone  = anketa_data['phone']
    cv = anketa_data['cv']
    bot_user = User(name=name, city=city, phone=phone, cv=cv)

    db_session.add(bot_user)
    db_session.commit()

    return ConversationHandler.END


def anketa_dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю')
