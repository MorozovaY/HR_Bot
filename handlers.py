from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

def greet_user(update, context):
    print('Вызван /start')
    username = update.effective_user.first_name
    context.bot.sendPhoto(chat_id=update.effective_chat.id,
    photo='https://www.un.org/counterterrorism/sites/www.un.org.counterterrorism/files/styles/panopoly_image_full/public/featured-page-we-do-cyber.jpg?itok=xkN5t0Rm',
    caption=f'Привет, {username}! Я бот компании Х, который поможет тебе лучше узнать о нас и наших возможностях. '
    'Для более расширенных возможностей нужно пройти маленькую регистрацию, нажав на кнопку ниже.',
        reply_markup=main_keyboard()
    )

def main_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Регистрация'],
            ['О компании'],
            ['Офисы'],
            ['Соцсети и контакты']
        ])


def company(update, context):
    update.message.reply_text(
        'Здесь будет информация о компании',
        reply_markup=main_keyboard()
    )

def offices(update, context):
    update.message.reply_text(
        'Здесь будет информация про офисы и филиалы',
        reply_markup=main_keyboard()
    )

def contacts_inline_keyboard():
    inlinekeyboard = [
        [
            InlineKeyboardButton('Instagram', url='https://www.instagram.com/?hl=ru'),
            InlineKeyboardButton('Facebook', url='https://ru-ru.facebook.com/')
        ]
    ]
    return InlineKeyboardMarkup(inlinekeyboard)

def contacts(update, context):
    update.message.reply_text(
        'Наши основные соцсети и контакты:',
        reply_markup=contacts_inline_keyboard()
    )