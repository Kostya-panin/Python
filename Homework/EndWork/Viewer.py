def maindialog():
    print("Что вы хотите сделать? Введите соответствующую цифру с клавиатуры:\n\
1. Получить список заметок\n\
2. Создать заметку\n\
0. Выход из программы")
    return input()

def dialoglistnotes():
    print("Что вы хотите сделать? Введите соответствующую цифру с клавиатуры:\n\
1. Редактировать заметку\n\
2. Прочитать заметку\n\
3. Удалить заметку\n\
0. Выход из программы")
    return input()

def dialognamenote():
    print("Введите имя заметки без расширения:")
    return input()

def dialogbodynote():
    print("Введите тело заметки:")
    return input()

def dialogtitlenote():
    print("Введите заголовок заметки:")
    return input()

def dialogfiltermotes():
    print("Как вы хотите отобразить заметки:\n\
1. Показать все заметки\n\
2. Отфильтровать по дате")
    return input()

def dialogeditnote():
    print("Что вы хотите сделать? Введите соответствующую цифру с клавиатуры:\n\
1. Редактировать заметку затерев данные полей\n\
2. Редактировать заметку дополнив данные полей")   

def inputinfo():
    print("Введите ФИО, номер, описание человека заносимого в телефонную книгу или 0 для выхода")
    info=input()
    return info
#Функция для вывода данных и запроса данных от пользователя
def userinput(data):
    print(data)
    return input()

def outputinfo(data):
    print(data)
#def printnoteslist():
    #print("В списке сохраненных есть следующие заметки:\n")

#info=dialog()
#print(type(info))


