from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import os

def hr_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Просмотр резюме', 'Просмотр пользователей'],
            ['Создать ключ кандидата и сотрудника'],
            ['Вернуться в главное меню']
        ])


def show_cv(update, context):
    files = os.listdir('downloads')
    for fl in files:
	    update.message.reply_document(document=open('downloads/'+fl,'rb'))
    update.message.reply_text('', reply_markup=hr_keyboard())


def roles_inline_keyboard():
    keyboard = [
        
            [InlineKeyboardButton("Внешний пользователь", callback_data='r1')],
            [InlineKeyboardButton("Кандидат", callback_data='r2')],
            [InlineKeyboardButton("Сотрудник", callback_data='r3')],
            
    ]
    return InlineKeyboardMarkup(keyboard)


def show_user(update, context):
    update.message.reply_text('Выберите роль', reply_markup=roles_inline_keyboard())
