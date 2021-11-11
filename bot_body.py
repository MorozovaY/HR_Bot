import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from handlers import greet_user, company, offices, contacts
from anketa import anketa
from external_keyboard import career, news, company_external, offices_external, back
from candidate_keyboard import dresscode, corplife, employment, adaptation
from employee_keyboard import questions, learning, development, referral, inline_buttons
from hr_keyboard import show_cv, show_user
from hr_dialog import add_user
from key_handler import enter_key_user
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(anketa)
    dp.add_handler(enter_key_user)
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CallbackQueryHandler(inline_buttons))
    dp.add_handler(MessageHandler(Filters.regex('^(О компании)$'), company))
    dp.add_handler(MessageHandler(Filters.regex('^(Про компанию)$'), company_external))
    dp.add_handler(MessageHandler(Filters.regex('^(Офисы)$'), offices))
    dp.add_handler(MessageHandler(Filters.regex('^(Наши офисы)$'), offices_external))
    dp.add_handler(MessageHandler(Filters.regex('^(Соцсети и контакты)$'), contacts))
    dp.add_handler(MessageHandler(Filters.regex('^(Карьера в компании)$'), career))
    dp.add_handler(MessageHandler(Filters.regex('^(Подписаться на новости)$'), news))
    dp.add_handler(MessageHandler(Filters.regex('^(Вернуться в главное меню)$'), back))
    dp.add_handler(MessageHandler(Filters.regex('^(Дресс-код)$'), dresscode))
    dp.add_handler(MessageHandler(Filters.regex('^(Корпоративная жизнь)$'), corplife))
    dp.add_handler(MessageHandler(Filters.regex('^(Трудоустройство)$'), employment))
    dp.add_handler(MessageHandler(Filters.regex('^(Адаптация)$'), adaptation))
    dp.add_handler(MessageHandler(Filters.regex('^(Вопросы в HR)$'), questions))
    dp.add_handler(MessageHandler(Filters.regex('^(Обучение)$'), learning))
    dp.add_handler(MessageHandler(Filters.regex('^(План развития)$'), development))
    dp.add_handler(MessageHandler(Filters.regex('^(Реферральная программа)$'), referral))
    dp.add_handler(MessageHandler(Filters.regex('^(Просмотр резюме)$'), show_cv))
    dp.add_handler(MessageHandler(Filters.regex('^(Просмотр пользователей)$'), show_user))
    dp.add_handler(add_user)
    

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
