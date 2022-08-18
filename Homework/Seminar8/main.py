database = {}
db={'parents':1,'children':2,'parents_telephone_numbers':3,'workshop':4,'workshop_and_child':5}
def reading_file_to_dict(number_file):
    with open (f'{number_file}.txt','r',encoding='utf-8') as file_1:
        data=([i.split('\n')[0]for i in file_1.readlines()])
        database[number_file]=[]
        for i in data:
            database[number_file].append(tuple(i.split(';')))
        #print(database)

def reading_files_to_dict(numberfiles):
    for i in range(1,numberfiles+1):
        #print(i)
        reading_file_to_dict(i)

def print_childrens(second_name):
    id=[i[0] for i in database[db['parents']] if second_name in i][0]
    deti=[i for i in database [db['children']]if id ==i[1]]
    print(*[' '.join(i[2:4])+'\n' for i in deti])

#Функция получения номера телефона родителя
def print_par_numbers(second_name):
    id=[i for i in database[db['parents']] if second_name in i]
    numbers=[i for i in database[db['parents_telephone_numbers']]if id[0][0] == i[1]]
    print('Номера родителя',*id[0][1:3],'\n',*[' '.join(i[2:4])+'\n' for i in numbers])

#Функция получения секции в которую ходит ребенок
def print_which_workshop(second_name,first_name):
    idchild=[i[0] for i in database[db['children']] if second_name and first_name in i][0]
    workshopid=[i[1] for i in database[db['workshop_and_child']]if idchild == i[0]]
    workshops=[i for i in database[db['workshop']]if i[0] in workshopid]
    print(second_name,first_name+'ходит в секции:'+'\n',*[''.join(i[1:2])+'\n' for i in workshops])

#Функция получения ребенка который ходит в определенную секцию
def print_who_workshop(Workshop):
    workshopid=[i[0] for i in database[db['workshop']] if Workshop in i][0]
    idchild=[i[0] for i in database[db['workshop_and_child']]if workshopid == i[1]][0]
    child=[i for i in database[db['children']] if idchild == i[0]]
    print('В секцию '+Workshop+' ходят :'+'\n',*[' '.join(i[2:4])+'\n' for i in child])


reading_files_to_dict(5)
print_who_workshop('Программирование')
#print_par_numbers('Иванов')
#print_which_workshop('Иванов','Егор')
#print_childrens('Иванов')
#reading_file_to_dict(2)
#print_childrens('Иванов')
