
# 1) Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# def itisfreeday(numberday):
#     if (numberday == 6) or (numberday == 7):
#         return 'Да'
#     else:
#         return 'Нет'
# print("Введите номер дня недели")
# numberday = int(input())
# print(itisfreeday(numberday))


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# def checkverity(x,y,z):
#     left = not (x or y or z)
#     right = not x and not y and not z
#     result = left == right
#     if result == True:
#         print(f"Утверждение истинно")
#     else:
#         print(f"Утверждение ложно")
# print("Введите переменные x,y,z")
# x,y,z=map(int, input().split())
# checkverity(x,y,z)

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def quarternumber(x,y):
#     if (x > 0) and (y > 0):
#         print("2 четверть")
#     if (x<0) and (y > 0):
#         print ("1 Четверть")
#     if (x>0) and (y <0):
#         print ("3 четверть")
#     if (x<0) and (y<0):
#         print ("4 четверть")
# print("Введите X")
# x=int(input())
# print ("Ввведите y")
# y=int(input())
# quarternumber(x,y)


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# def range(number):
#     if number == 1:
#         print("x<0 y>0")
#     if number == 2:
#         print("x>0 y>0")
#     if number == 3:
#         print("x>0 y<0")
#     if number == 4:
#         print("x<0 y<0")
# print("Введите номер четверти")
# number = int(input())
# range(number)

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# from cmath import sqrt
# def distance(Ax,Ay,Bx,By):
#     AB=sqrt((pow((Bx-Ax),2))+(pow((By-Ay),2)))
#     print(AB)
# print("Введите черз пробел координаты точек Ax, Ay, Bx ,By")
# Ax,Ay,Bx,By=map(int,input().split())
# distance(Ax,Ay,Bx,By)


