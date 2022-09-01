import Viewer
import Worker
import Loger
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import json
# Определяем константы этапов разговора
STATE0, STATE1, STATE2, STATE3, STATE4 = range(5)

    # функция обратного вызова точки входа в разговор и просьба о вводе первого числа
def start(update, _):
    update.message.reply_text("Привет я бот который импортирует и экспортирует данные из телефонной книги. Введи что угодно и я начну работать")
    return STATE0

#Записываем второе число в переменную и просим ввести действие
def input0(update, _):
    update.message.reply_text(
  "Что вы хотите сделать? Введите соответствующую цифру с клавиатуры:\n\
1. Поучить данные из телефонной книги\n\
2. Занести данные в телефонную книгу\n\
Введите команду cancel для выхода")
    return STATE1

# Записываем первое число в переменную и просим ввести воторое число
def input1(update, _):
    global num
    num=update.message.text
    if num == "1":
        data=json.dumps(Worker.export_from_phonebook(),ensure_ascii=False)
        update.message.reply_text(data)
        return STATE0
    if num == "2":
        update.message.reply_text("Введите ФИО, номер, описание человека заносимого в телефонную книгу")
        return STATE2

# Записываем второе число в переменную и просим ввести действие
def input2(update, _):
    data=update.message.text
    Worker.import_in_phonebook(data)
    Loger.createevent(data)
    return STATE3

 #Записываем операцию в переменную и пишем щас посчитаю
def input3(update, _):
    
    return ConversationHandler.END

# # Обрабатываем команду /cancel
def cancel(update, _):
    update.message.reply_text("Пока!!!!")
    return ConversationHandler.END

if __name__ == '__main__':
# Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("5195282354:AAFrqfAo1G302KjG4nzjhXJSxQzubO48eQo")
# получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

# Определяем обработчик разговоров `ConversationHandler` 
    conv_handler = ConversationHandler(
# точка входа
    entry_points=[CommandHandler('start', start)],
# этапы
    states={
        STATE0: [MessageHandler(Filters.text & ~Filters.command, input0)],
        STATE1: [MessageHandler(Filters.text & ~Filters.command, input1)],
        STATE2: [MessageHandler(Filters.text & ~Filters.command, input2)],
        STATE3: [MessageHandler(Filters.text & ~Filters.command, input3)],
    },
# точка выхода
    fallbacks=[CommandHandler('cancel', cancel)],
        )

# Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

# Запуск бота
    updater.start_polling()
    updater.idle()