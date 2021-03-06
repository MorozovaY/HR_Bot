from telegram import ReplyKeyboardRemove
from telegram.ext import  ConversationHandler
from key_handler import send_key
from handlers import main_keyboard
from external_keyboard import external_keyboard
from sqlalchemy.exc import IntegrityError
import re
import os
from other import external_photo
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext import MessageHandler,CommandHandler, Filters

from db import db_session
from db import User


def anketa_start(update, context):
    context.user_data['anketa'] = dict()
    update.message.reply_text(
        'Вы перешли в раздел регистрация.'
        'Пожалуйста, введите, как Вас зовут через пробел в формате: ФАМИЛИЯ ИМЯ ОТЧЕСТВО.',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'


def anketa_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 3:
        update.message.reply_text('Пожалуйста, введите фамилию, имя и отчество.')
        return 'name'
    else:
        context.user_data['anketa']['name'] = update.message.text
        update.message.reply_text(
            'Введите город проживания.'
        )
        return 'city'


def anketa_city(update, context):
    user_city = update.message.text
    list(user_city)
    if user_city[0].isdigit() is False:
        context.user_data['anketa']['city'] = user_city
        update.message.reply_text('Введите телефон для связи.')
        return 'phone'
    else:
        update.message.reply_text('Пожалуйста, введите название города корректно.')
        return 'city'


def anketa_phone(update, context):
    user_phone = update.message.text
    phone_check = bool(re.findall(r"(^8|\+7)((\d{10})|(\s\(\d{3}\)\s\d{3}\s\d{2}\s\d{2}))", user_phone))
    if  phone_check is True:
        context.user_data['anketa']['phone'] = user_phone
        update.message.reply_text(
            'Вы можете прикрепить Ваше резюме файлом в формате .pdf '
            'Либо можете пропустить этот этап нажав /skip'
            )
        return 'cv'
    else:
        update.message.reply_text('Пожалуйста, введите номер телефона в формате: +7ХХХХХХХХХХ либо 8 ХХХ ХХХ ХХ ХХ.')
        return 'phone'


def anketa_cv(update, context):
    cv_name = update.message.document.file_name
    cv_check = cv_name.split('.')
    anketa_data = context.user_data.get('anketa')
    if anketa_data is None:
        update.message.reply_text('Не удалось сохранить анкету.')
        return ConversationHandler.END
    if cv_check[-1] != 'pdf':
        update.message.reply_text('Ошибка. Программа принимает только файлы формата pdf.')
        return 'anketa_cv'
    if cv_check[-1] == 'pdf':
        os.makedirs('downloads', exist_ok=True)
        cv_file = context.bot.getFile(update.message.document.file_id)
        filename = os.path.join('downloads', f'{cv_file.file_id}.pdf')
        cv_file.download(filename)
        context.user_data['anketa']['role'] = 'external'

    bot_user = User(
        name=anketa_data.get('name'), 
        city=anketa_data.get('city'), 
        phone=anketa_data.get('phone'), 
        cv=anketa_data.get('cv')
    )

    try:
        db_session.add(bot_user)
        db_session.commit()
        context.bot.sendPhoto(chat_id=update.effective_chat.id,
        photo=external_photo,
        caption='Регистрация успешно завершена! Ниже представлено меню бота для Вас.',
        reply_markup=external_keyboard()
        )
        send_key(update, context)
        
    except IntegrityError:
        update.message.reply_text('Ошибка. Такой номер телефона уже зарегестрирован.',
            reply_markup=main_keyboard()
        )
        db_session.rollback()
            
    return ConversationHandler.END


def anketa_cv_skip(update, context):
    context.user_data['anketa']['role'] = 'external'
    anketa_data = context.user_data.get('anketa')
    bot_user = User(
        name=anketa_data.get('name'), 
        city=anketa_data.get('city'), 
        phone=anketa_data.get('phone'), 
        cv=anketa_data.get('cv')
    )

    try:
        db_session.add(bot_user)
        db_session.commit()
        context.bot.sendPhoto(chat_id=update.effective_chat.id,
        photo=external_photo,
        caption='Регистрация успешно завершена! Ниже представлено меню бота для Вас.',
        reply_markup=external_keyboard()
    )
    except IntegrityError:
        update.message.reply_text('Ошибка. Такой номер телефона уже зарегестрирован.',
            reply_markup=main_keyboard()
        )
        db_session.rollback()
    update.message.reply_text(
        'Регистрация завершена без сохранения резюме.',
        send_key(update, context),
        reply_markup=external_keyboard()
        
    )
    return ConversationHandler.END


def anketa_dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю.')


anketa = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Регистрация)$'), anketa_start)
        ],
    states={
        'name': [MessageHandler(Filters.text, anketa_name)],
        'city': [MessageHandler(Filters.text, anketa_city)],
        'phone': [MessageHandler(Filters.text, anketa_phone)],
        'cv' : [
            CommandHandler("skip", anketa_cv_skip),
            MessageHandler(Filters.document, anketa_cv)
        ]
            
        },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, anketa_dontknow)
    ]
)
