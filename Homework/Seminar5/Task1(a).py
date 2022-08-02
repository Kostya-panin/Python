#вариант с ботом
import random
player1=1
player2=1
NumOfCandPlayer1=1
NumOfCandPlayer2=1
lasthod=0
while ((NumOfCandPlayer1+NumOfCandPlayer2)<50) and not player1==0 and not player2==0:
    while ((NumOfCandPlayer1+NumOfCandPlayer2)<50):
        player1=1
        player1=int(input("Ход первого игрока: Введите количество конфет или 0 для выхода: "))
        if (player1>28):
            print("Нельзя брать более 28 конфет за раз!!!")
        else:
            NumOfCandPlayer1=NumOfCandPlayer1+player1
            lasthod=1
            break
    botnumber=random.randint(1,28)
    NumOfCandPlayer2=NumOfCandPlayer2+botnumber
    print("Бот ввел",botnumber)
    lasthod=2
if (lasthod==1):
    print("Выиграл первый игрок")
else:
    print("Выиграл Бот")