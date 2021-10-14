from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from candidate_keyboard import candidate_keyboard

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
            ['Войти по ключу кандидата'],
            ['О компании', 'Офисы', 'Соцсети и контакты']
        ])


def enter_candidate(update, context):
    context.bot.sendPhoto(chat_id=update.effective_chat.id,
    photo='https://previews.123rf.com/images/maxkabakov/maxkabakov1210/maxkabakov121000043/15856739-%E6%83%85%E5%A0%B1%E6%8A%80%E8%A1%93-it-%E3%81%AE%E6%A6%82%E5%BF%B5-%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB-%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%80%813-d-%E3%81%AE%E3%83%AC%E3%83%B3%E3%83%80%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%AB%E3%83%94%E3%82%AF%E3%82%BB%E3%83%AB%E5%8C%96%E3%81%95%E3%82%8C%E3%81%9F%E8%A8%80%E8%91%89%E3%82%92%E6%AD%93%E8%BF%8E.jpg',
    caption='Поздравляем с успешным прохождением всех этапов отбора! Ниже представлено меню бота для Вас.',
    reply_markup=candidate_keyboard()
)


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
