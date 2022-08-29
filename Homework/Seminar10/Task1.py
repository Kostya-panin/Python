from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import random
player1=1
player2=1
NumOfCandPlayer1=1
NumOfCandPlayer2=1
lasthod=0


# Определяем константы этапов разговора
STATE0, STATE1, STATE2, STATE3, STATE4 = range(5)


    # функция обратного вызова точки входа в разговор
def start(update, _):
    update.message.reply_text("Привет!! Я бот!! Поиграем в конфеты?\nВведи количество конфет которое ты хочешь взять")
    return STATE0

def input0(update, _):
    global player1
    global NumOfCandPlayer1
    global lasthod
    global NumOfCandPlayer2
    player1=int(update.message.text)
    if (player1>28):
        update.message.reply_text("Нельзя брать более 28 конфет за раз!!!\nВведи количество конфет которое ты хочешь взять")
        update.message.reply_text("Введи количество конфет которое ты хочешь взять")
        player1=0
        return STATE0
    else:
        NumOfCandPlayer1=NumOfCandPlayer1+player1
        lasthod=1
        if (NumOfCandPlayer1+NumOfCandPlayer2)>2021:
            if (lasthod==1):
                update.message.reply_text("Ты выиграл!!!")
            else:
                update.message.reply_text("Я выиграл")
            return ConversationHandler.END
        else:
            botnumber=random.randint(1,28)
            NumOfCandPlayer2=NumOfCandPlayer2+botnumber
            update.message.reply_text(f"Я возьму {botnumber} конфет")
            lasthod=2
            if (NumOfCandPlayer1+NumOfCandPlayer2)>2021:
                if (lasthod==1):
                    update.message.reply_text("Ты выиграл!!!")
                else:
                    update.message.reply_text("Я выиграл")
                return ConversationHandler.END
            else:
                update.message.reply_text("Введи количество конфет которое ты хочешь взять")
                return STATE0

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
        # STATE1: [MessageHandler(Filters.text & ~Filters.command, input1)],
        # STATE2: [MessageHandler(Filters.text & ~Filters.command, input2)],
        # STATE3: [MessageHandler(Filters.text & ~Filters.command, input3)],
    },
# точка выхода
    fallbacks=[CommandHandler('cancel', cancel)],
        )

# Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

# Запуск бота
    updater.start_polling()
    updater.idle()