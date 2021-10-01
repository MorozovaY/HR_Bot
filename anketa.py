from telegram import ReplyKeyboardRemove
from telegram.ext import  ConversationHandler
from handlers import main_keyboard

def anketa_start(update, context):
    update.message.reply_text(
        'Вы перешли в раздел регистрация.'
        'Пожалуйста введите как Вас зовут через пробел в формате: ФАМИЛИЯ ИМЯ ОТЧЕСТВО',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'

def anketa_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 3:
        update.message.reply_text('Пожалуйста введите имя, фамилию и отчество')
        return 'name'
    else:
        context.user_data['anketa']['name'] = update.message.text
        update.message.reply_text(
            'Введите город проживания'
        )
        return 'city'

def anketa_city(update, context):
    context.user_data['anketa']['city'] = update.message.text
    update.message.reply_text('Введите телефон для связи')
    return 'phone'

def anketa_phone(update, context):
    context.user_data['anketa']['phone'] = update.message.text
    update.message.reply_text(
        'Вы можете прикрепить Ваше резюме файлом в формате .pdf'
        'Либо можете пропустить этот этап нажав /skip'
    )
    return 'cv'

def anketa_cv(update, context):
    context.user_data['anketa']['cv'] = update.message.text
    update.message.reply_text(
        'Регистрация завершена.',
        reply_markup=main_keyboard()
    )
    return ConversationHandler.END

def anketa_dontknow(update, context):
    update.message.reply_text('Я вас не понимаю')

#Прикрепить резюме + skip#

#внешний человек/кандидат/сотрудник) все данные складывать складывать в context.user_data#