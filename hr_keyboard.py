from sqlalchemy.sql.expression import table
from telegram import ReplyKeyboardMarkup, ParseMode

import prettytable as pt
import os

from db import db_session
from db import User

def hr_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Просмотр резюме', 'Просмотр пользователей'],
            ['Создать ключ кандидата', 'Создать ключ сотрудника'],
            ['Вернуться в главное меню']
        ])


def show_cv(update, context):
    files = os.listdir('downloads')
    for fl in files:
	    update.message.reply_document(document=open('downloads/'+fl,'rb'))
    update.message.reply_text('', reply_markup=hr_keyboard())


def show_user(update, context):
    table = pt.PrettyTable(['Имя', 'Город', 'Телефон'])
    table.align['Имя'] = 'l'
    table.align['Город'] = 'r'
    table.align['Телефон'] = 'r'

    for row in db_session.query(User):
        table.add_row([row.name, row.city, row.phone])
    update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML, reply_markup=hr_keyboard())


def candidate_key(update, context):
    update.message.reply_text(
        'Здесь должен быть диалог, в котором HR создает ключ кандидата',
        reply_markup=hr_keyboard()
    )


def employee_key(update, context):
    update.message.reply_text(
        'Здесь должен быть диалог, в котором HR создает ключ сотрудника',
        reply_markup=hr_keyboard()
    )
