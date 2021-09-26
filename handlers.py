from telegram import ReplyKeyboardMarkup, KeyboardButton

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text(
        'Я бот компании Х, который поможет тебе лучше узнать о нас и траляля',
        reply_markup=main_keyboard()
    )

def main_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Зарегестрироваться'],
            ['О компании', 'Офисы'],
            ['Соцсети и контакты']
        ])
        
def regist(update, context):
    update.message.reply_text(
        'Вы нажали на кнопку Зарегестрироваться',
        reply_markup=main_keyboard()
    )

def company(update, context):
    update.message.reply_text(
        'Вы нажали на кнопку О компании',
        reply_markup=main_keyboard()
    )

def offices(update, context):
    update.message.reply_text(
        'Вы нажали на кнопку Офисы',
        reply_markup=main_keyboard()
    )

def contacts(update, context):
    update.message.reply_text(
        'Вы нажали на кнопку Соцсети и контакты',
        reply_markup=main_keyboard()
    )