from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import prettytable as pt
from db import db_session, User

def employee_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Вопросы в HR', 'Обучение'],
            ['План развития', 'Реферральная программа'],
            ['Вернуться в главное меню']
        ])


def questions_inline_keyboard():
    keyboard = [
        
            [InlineKeyboardButton("Question 1", callback_data='1')],
            [InlineKeyboardButton("Question 2", callback_data='2')],
    ]
    return InlineKeyboardMarkup(keyboard)


def inline_buttons(update, context):
    query = update.callback_query
    query.answer()
    chat_id = update.callback_query.message.chat.id
    if query.data == "1":
        context.bot.sendMessage(chat_id, 'Answer 1', reply_markup=questions_inline_keyboard())
    if query.data == "2":
        context.bot.sendMessage(chat_id, 'Answer 2', reply_markup=questions_inline_keyboard())
    if query.data == "r1":
        context.bot.sendMessage(chat_id, f'<pre>{show_users_by_role(0).get_string()}</pre>', parse_mode=ParseMode.HTML)
    if query.data == "r2":
        context.bot.sendMessage(chat_id, f'<pre>{show_users_by_role(1).get_string()}</pre>', parse_mode=ParseMode.HTML)
    if query.data == "r3":
        context.bot.sendMessage(chat_id, f'<pre>{show_users_by_role(2).get_string()}</pre>', parse_mode=ParseMode.HTML)  


def show_users_by_role(role):
    table = pt.PrettyTable(['Имя', 'Город', 'Телефон'])
    table.align['Имя'] = 'l'
    table.align['Город'] = 'r'
    table.align['Телефон'] = 'r'

    for row in db_session.query(User).filter(User.role == role):
        table.add_row([row.name, row.city, row.phone])
    return table


def questions(update, context):
    update.message.reply_text(
        'Здесь будут ответы на HR вопросы',
        reply_markup=questions_inline_keyboard()
    )


def learning(update, context):
    update.message.reply_text(
        'Здесь будет информация про курсы и обучение',
        reply_markup=employee_keyboard()
    )


def development(update, context):
    update.message.reply_text(
        'Здесь будет индивидуальный план развития',
        reply_markup=employee_keyboard()
    )


def referral(update, context):
    update.message.reply_text(
        'Здесь будет описание реферральной программы и возможность отправить резюме друга в HR',
        reply_markup=employee_keyboard()
    )
