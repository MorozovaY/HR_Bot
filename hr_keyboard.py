from telegram import ReplyKeyboardMarkup

def hr_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Просмотр резюме', 'Просмотр пользователей'],
            ['Создать ключ кандидата', 'Создать ключ сотрудника'],
            ['Вернуться в главное меню']
        ])


def show_cv(update, context):
    update.message.reply_text(
        'При нажатии кнопки HR может просматривать прикрепленные резюме',
        reply_markup=hr_keyboard()
    )


def show_user(update, context):
    update.message.reply_text(
        'При нажатии кнопки HR может просматривать зарегистрированных пользователей, кандидатов и сотрудников',
        reply_markup=hr_keyboard()
    )


def candidate_key(update, context):
    update.message.reply_text(
        'Здесь должен быть диалог, в котором HR создает ключ кандидата',
        reply_markup=hr_keyboard()
    )


def employee_key(update, context):
    update.message.reply_text(
        'Здесь должен быть диалог, в котором HR создает ключ сотрудника',
        reply_markup=hr_keyboard()
    )
