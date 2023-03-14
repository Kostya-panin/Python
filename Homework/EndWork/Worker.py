import os
import json
from datetime import datetime as dt
import uuid
from json import JSONEncoder
from uuid import UUID
old_default = JSONEncoder.default

def new_default(self, obj):
    if isinstance(obj, UUID):
        return str(obj)
    return old_default(self, obj)

JSONEncoder.default = new_default
#Функция для записи данных в файл
def import_in_phonebook(data):
    with open('Main_phone_book.txt','a',encoding='utf-8') as file:
        data=file.writelines(f'{data}\n')
#Функция для чтения данных из файла
def read_note(name):
    with open('Notes//'+name+'.json','r',encoding='utf-8') as file:
        data=file.read()
    return data
#Функция для получения списка заметок
def get_list_notes(path):
    data=os.listdir(path)
    return data
#Функция для получения фильтрованного по дате списка заметок
def get_filter_list_notes(path):
    data=os.path.getctime(path)
    return data
#Функция для удаления заметки
def remove_note(name):
    os.remove('Notes//'+name+'.json')
#Функция для создания новой заметки
def new_note(name,title,body):
    date=dt.now().strftime('%D %H:%M')
    id=uuid.uuid4()
    dictionary={'title':title,'body':body,'createdate':date,'editdate':date,'id':id}
    jsonstring=json.dumps(dictionary,indent=4,ensure_ascii=False)
    with open('Notes//'+name+'.json','w',encoding='utf-8') as file:
        file.writelines(f'{jsonstring}\n')
    return 0
#функция для редактирования заметки c перезаписью полей
def edit_note(name,title,body):
    date=dt.now().strftime('%D %H:%M')
    with open('Notes//'+name+'.json') as fp:
        data = json.load(fp)
    data['title'] = title
    data['body'] = body
    data['editdate'] = date
    with open('Notes//'+name+'.json', 'w',encoding='utf-8') as fp:
        json.dump(data,fp,indent=4,ensure_ascii=False)



