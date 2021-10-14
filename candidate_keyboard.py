from telegram import ReplyKeyboardMarkup

def candidate_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Дресс-код', 'Корпоративная жизнь'],
            ['Трудоустройство', 'Адаптация'],
            ['Вернуться в главное меню']
        ])


def dresscode(update, context):
    update.message.reply_text(
        'Здесь будет информация про дресс-код',
        reply_markup=candidate_keyboard()
    )


def corplife(update, context):
    update.message.reply_text(
        'Здесь будет информация про мероприятия и активности компании',
        reply_markup=candidate_keyboard()
    )


def employment(update, context):
    update.message.reply_text(
        'Здесь будет информация про документы для трудоустройства',
        reply_markup=candidate_keyboard()
    )


def adaptation(update, context):
    update.message.reply_text(
        'Здесь будет информация про адаптацию',
        reply_markup=candidate_keyboard()
    )
