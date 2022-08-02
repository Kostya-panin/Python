# Создайте программу для игры в ""Крестики-нолики"".
# функция для рисования поля крестики нолики
def drawingField(FieldState):
    print("Игровое поле")
    for row in FieldState:
        for elem in row:
                print(elem, end=' ')
        print("")
#Функция для изменения ячеек на игровом поле
def Setfieldstate(fieldstate,player):
    print(f"{player} введите координата1 координата2 и значек которым вы играете через пробел")
    a,b,c=input().split(' ')
    fieldstate[int(a)][int(b)]=str(c)
    return fieldstate
#функция для проверки выигрыша в игре
def check(fieldstate,symbol):
    if(fieldstate[0][0]==fieldstate[0][1]==fieldstate[0][2]==f"{symbol}"
        or fieldstate[1][0]==fieldstate[1][1]==fieldstate[1][2]==f"{symbol}"\
        or fieldstate[2][0]==fieldstate[2][1]==fieldstate[2][2]==f"{symbol}"\
        or fieldstate[0][0]==fieldstate[1][0]==fieldstate[2][0]==f"{symbol}"\
        or fieldstate[0][1]==fieldstate[1][1]==fieldstate[2][1]==f"{symbol}"\
        or fieldstate[0][2]==fieldstate[1][2]==fieldstate[2][2]==f"{symbol}"\
        or fieldstate[0][0]==fieldstate[1][1]==fieldstate[2][2]==f"{symbol}"\
        or fieldstate[0][2]==fieldstate[1][1]==fieldstate[2][0]==f"{symbol}"):
        return symbol
    else:
        return 1
fieldstate = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
i=0
while i<9:
    if (check(fieldstate,"0"))=="0":
        print("Выиграл игрок играющий ноликами!!!!!")
        break
    if (check(fieldstate,"x"))=="x":
        print("Выиграл игрок играющий крестиками!!!!!")
        break
    Setfieldstate(fieldstate,"Игрок играющий ноликами, ")
    i=i+1
    if i >=9:
        print ("Ничья!!!!!!")
        break
    print()
    drawingField(fieldstate)
    print()
    Setfieldstate(fieldstate,"Игрок играющий крестиками, ")
    i=i+1
    if i >=9:
        print ("Ничья!!!!!!")
        break
    print()
    drawingField(fieldstate)
    print()
