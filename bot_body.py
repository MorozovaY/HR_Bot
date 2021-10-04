import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from handlers import greet_user, regist, company, offices, contacts_inline_keyboard, contacts
from anketa import anketa_start, anketa_name, anketa_city, anketa_phone, anketa_cv, anketa_dontknow


import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher

    anketa = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Регистрация)$'), anketa_start)
        ],
        states={
            'name': [MessageHandler(Filters.text, anketa_name)],
            'city': [MessageHandler(Filters.text, anketa_city)],
            'phone': [MessageHandler(Filters.text, anketa_phone)],
            'cv' : [MessageHandler(Filters.text, anketa_cv)]
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, anketa_dontknow)
        ]
    )
    dp.add_handler(anketa)
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CallbackQueryHandler(contacts_inline_keyboard))
    dp.add_handler(MessageHandler(Filters.regex('^(О компании)$'), company))
    dp.add_handler(MessageHandler(Filters.regex('^(Офисы)$'), offices))
    dp.add_handler(MessageHandler(Filters.regex('^(Соцсети и контакты)$'), contacts))


    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()     