def dialog():
    print("Что вы хотите сделать? Введите соответствующую цифру с клавиатуры:\n\
1. Поучить данные из телефонной книги\n\
2. Занести данные в телефонную книгу\n\
0. Выход из программы")
    # userinput=input()
    # return userinput
    return input()

def inputinfo():
    print("Введите ФИО, номер, описание человека заносимого в телефонную книгу или 0 для выхода")
    info=input()
    return info

def outputinfo(data):
    print(data)

#info=dialog()
#print(type(info))
