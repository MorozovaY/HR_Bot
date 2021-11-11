from cryptography.fernet import Fernet
from external_keyboard import external_keyboard
from candidate_keyboard import candidate_keyboard
from employee_keyboard import employee_keyboard
from hr_keyboard import hr_keyboard
from settings import CYPHER_KEY
from other import external_photo, candidate_photo, employee_photo, hr_photo
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext import MessageHandler, Filters


def send_key(update, context):
    anketa_data = context.user_data.get('anketa')
    phone = str(anketa_data.get('phone'))
    role = anketa_data.get('role')
    cipher = Fernet(CYPHER_KEY)
    combined_data = phone + '...' + role
    byte_text = str.encode(combined_data)
    encrypted_bytekey = cipher.encrypt(byte_text) 
    encrypted_key = encrypted_bytekey.decode()  # это  ключ доступа
    update.message.reply_text(
        'Следующим сообщением вам будет выслан ключ для доступа к дополнительным функциям бота. '
        'Чтобы использовать ключ, скопируйте его, нажмите кнопку "Войти по ключу", вставьте его в сообщение и отправьте боту'
    )
    update.message.reply_text(f'{encrypted_key}')


def receive_key(update, context):
    update.message.reply_text('Введите ключ доступа')
    return 'user_key'

def check_user_key(update, context):
    user_key = update.message.text
    cipher = Fernet(CYPHER_KEY)
    user_bytekey = str.encode(user_key)
    decrypted_key = cipher.decrypt(user_bytekey)
    combined_data = decrypted_key.decode()
    check_combined_data = combined_data.split('...')
    if check_combined_data[-1] == 'external':
        context.bot.sendPhoto(chat_id=update.effective_chat.id,
        photo=external_photo,
        caption='Поздравляем с успешным прохождением регистрации! Ниже представлено меню бота для Вас.',
        reply_markup=external_keyboard())
        return ConversationHandler.END

    elif check_combined_data[-1] == 'candidate':
        context.bot.sendPhoto(chat_id=update.effective_chat.id,
        photo=candidate_photo,
        caption='Поздравляем с успешным прохождением всех этапов отбора! Ниже представлено меню бота для Вас.',
        reply_markup=candidate_keyboard())
        return ConversationHandler.END

    elif check_combined_data[-1] == 'employee':
        context.bot.sendPhoto(chat_id=update.effective_chat.id,
        photo=employee_photo,
        caption='Welcome on board! Ниже представлено меню бота для Вас.',
        reply_markup=employee_keyboard())
        return ConversationHandler.END

    elif check_combined_data[-1] == 'HR':
        context.bot.sendPhoto(chat_id=update.effective_chat.id,
        photo=hr_photo,
        caption='Ниже представлено меню бота для HR.',
        reply_markup=hr_keyboard())
        return ConversationHandler.END

def enter_user_dontknow(update, context):
    update.message.reply_text('Я Вас не понимаю.')

enter_key_user = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Войти по ключу)$'), receive_key)
        ],
    states={
        'user_key': [MessageHandler(Filters.text, check_user_key)],

    },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, enter_user_dontknow)
    ]
)
