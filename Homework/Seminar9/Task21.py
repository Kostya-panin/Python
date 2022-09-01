from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Определяем константы этапов разговора
STATE0, STATE1, STATE2, STATE3, STATE4 = range(5)
#Функция калькулятора
def calc(num1,num2,oper):
    if 'j' in num1:
        num1=complex(num1)
    else:
        num1=int(num1)
    if 'j' in num2:
        num2=complex(num2)
    else:
        num2=int(num2)
    if oper == "+":
        res1=num1+num2
    if oper == "-":
        res1=num1-num2
    if oper == "*":
        res1=num1*num2
    if oper == "/":
            res1=num1/num2   
    return res1

# функция обратного вызова точки входа в разговор и просьба о вводе первого числа
def start(update, _):
    update.message.reply_text(
        'Привет я бот калькулятор напиши мне что угодно и начнем считать!!! ')
    #переходим к этапу STATE0
    return STATE0

# Записываем второе число в переменную и просим ввести действие
def input0(update, _):
    update.message.reply_text(
        'Введите первое число рациональное или комплексное')
    # переходим к этапу `STATE1`
    return STATE1

# Записываем первое число в переменную и просим ввести воторое число
def input1(update, _):
    global num1
    num1=update.message.text
    if not(num1.isdigit() or "j" in num1):
        update.message.reply_text(
        'Неверный ввод! Необходимо вводить рациональное или комплексное число')
        return STATE1
    update.message.reply_text(
        'Введите второе число рациональное или комплексное')
    # переходим к этапу `STATE2`
    return STATE2

# Записываем второе число в переменную и просим ввести действие
def input2(update, _):
    global num2
    num2=update.message.text
    if not(num2.isdigit() or "j" in num2):
        update.message.reply_text(
        'Неверный ввод! Необходимо вводить рациональное или комплексное число')
        return STATE2
    update.message.reply_text(
        'Введите действие: + - * /')
    # переходим к этапу `LOCATION`
    return STATE3

 #Записываем операцию в переменную и пишем щас посчитаю
def input3(update, _):
    update.message.reply_text(
        'щас посчитаю')
    global oper
    oper=update.message.text
    res=calc(num1,num2,oper)
    update.message.reply_text(f'Ответ: {str(res)}')
    return ConversationHandler.END

# # Обрабатываем команду /cancel
def cancel(update, _):
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