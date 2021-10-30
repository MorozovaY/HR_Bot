from sqlalchemy.sql.functions import user
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardRemove
import re
from db import db_session, User, Role
from hr_keyboard import hr_keyboard
from sqlalchemy.exc import IntegrityError


def add_user_start(update, context):
    context.user_data['new_user'] = dict()
    update.message.reply_text(
        'Вы перешли в раздел регистрации нового пользователя. '
        'Пожалуйста, введите имя нового пользователя в формате: ФАМИЛИЯ ИМЯ ОТЧЕСТВО.',
    reply_markup=ReplyKeyboardRemove()
    )
    return 'name'


def add_user_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 3:
        update.message.reply_text('Пожалуйста, введите фамилию, имя и отчество.')
        return 'name'
    else:
        context.user_data['new_user']['name'] = update.message.text
        update.message.reply_text(
            'Введите телефонный номер.'
        )
        return 'phone'


def add_user_phone(update, context):
    user_phone = update.message.text
    phone_check = bool(re.findall(r"(^8|\+7)((\d{10})|(\s\(\d{3}\)\s\d{3}\s\d{2}\s\d{2}))", user_phone))
    if phone_check is True:
        context.user_data['new_user']['phone'] = user_phone
        update.message.reply_text(
            'Введите роль пользователя. Доступные опции: "Кандидат" и "Сотрудник".')
        return 'role'


def add_user_role(update, context):
    user_role = update.message.text
    row = db_session.query(Role).filter(Role.role == user_role).first()
    if row is None:
        update.message.reply_text(
            'Роль не найдена. Введите снова!'
        )
        return 'role'
    context.user_data['new_user']['role'] = row.id
    user = context.user_data.get('new_user')

    bot_user = User(name=user.get('name'), phone=user.get('phone'), role=user.get('role'))

    try:
        db_session.add(bot_user)
        db_session.commit()
        update.message.reply_text('Создание пользователя завершено. ',
        generareply_markup=hr_keyboard())
    
    except IntegrityError:
        update.message.reply_text('Ошибка. Такой номер телефона уже зарегестрирован.',
            reply_markup=hr_keyboard()
        )
        db_session.rollback()

    return ConversationHandler.END


def add_user_dontknow (update, context):
    update.message.reply_text('Я Вас не понимаю.')


add_user = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Создать ключ кандидата и сотрудника)$'), add_user_start)
    ],
    states={
        'name': [MessageHandler(Filters.text, add_user_name)],
        'phone': [MessageHandler(Filters.text, add_user_phone)],
        'role': [MessageHandler(Filters.text, add_user_role)],
    },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, add_user_dontknow)
    ]
)
