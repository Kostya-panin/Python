# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""

player1=1
player2=1
NumOfCandPlayer1=1
NumOfCandPlayer2=1
lasthod=0
while ((NumOfCandPlayer1+NumOfCandPlayer2)<2021) and not player1==0 and not player2==0:
    while ((NumOfCandPlayer1+NumOfCandPlayer2)<2021):
        player1=1
        player1=int(input("Ход первого игрока: Введите количество конфет или 0 для выхода: "))
        if (player1>28):
            print("Нельзя брать более 28 конфет за раз!!!")
        else:
            NumOfCandPlayer1=NumOfCandPlayer1+player1
            lasthod=1
            break
    while ((NumOfCandPlayer1+NumOfCandPlayer2)<2021):
        player2=1
        player2=int(input("Ход Второго игрока: Введите количество конфет или 0 для выхода: "))
        if (player2>28):
            print("Нельзя брать более 28 конфет за раз!!!")
        else:
            NumOfCandPlayer2=NumOfCandPlayer2+player2
            lasthod=2
            break
if (lasthod==1):
    print("Выиграл первый игрок")
else:
    print("Выиграл второй игрок")


    


