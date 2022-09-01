#Функция для записи данных в файл
def import_in_phonebook(data):
    with open('Main_phone_book.txt','a',encoding='utf-8') as file:
        data=file.writelines(f'{data}\n')
#Функция для чтения данных из файла
def export_from_phonebook():
    with open('Main_phone_book.txt','r',encoding='utf-8') as file:
        data=file.read()
    return data