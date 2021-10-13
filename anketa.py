from telegram import ReplyKeyboardRemove
from telegram.ext import  ConversationHandler
from handlers import main_keyboard
from external_keyboard import external_keyboard
from sqlalchemy.exc import IntegrityError

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
    anketa_data = context.user_data.get('anketa')
    if anketa_data is None:
        update.message.reply_text('Не удалось сохранить анкету.')
        return ConversationHandler.END

    bot_user = User(name=anketa_data.get('name'), city=anketa_data.get('city'), phone=anketa_data.get('phone'), cv=anketa_data.get('cv'))

    try:
        db_session.add(bot_user)
        db_session.commit()
        context.bot.sendPhoto(chat_id=update.effective_chat.id,
        photo='https://media.kingston.com/kingston/hero/ktc-hero-solutions-data-security-who-is-responsible-for-cyber-security-lg.jpg',
        caption='Регистрация успешно завершена! Ниже представлено меню бота для Вас.',
        reply_markup=external_keyboard()
    )
    except IntegrityError:
        update.message.reply_text('Что-то пошло не так, попробуйте снова.',
            reply_markup=main_keyboard()
        )
        db_session.rollback()
            
    return ConversationHandler.END


def anketa_dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю')
