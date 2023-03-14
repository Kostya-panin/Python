from datetime import datetime as dt
def createevent(data):
    date=dt.now().strftime('%D %H:%M')
    with open('log.txt','a',encoding='utf-8') as file:
        file.writelines(f'{date} В телефонную книгу внесена запись: {data}\n')
