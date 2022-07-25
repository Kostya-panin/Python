#Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141
# Способ1
# import math
# number=math.pi
# print(round(number, 3))
# Способ2
# d = 3
# k = 1
# pi = 0
# for k in range(1, 100000):
#     pi = pi+4*((-1)**(k+1))/(2*k-1)
# print(round(pi, 5))

# Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)
# def IsPrime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
# def ListPrimeDiv(N):
#     i=2
#     for i in range(2,N+1):
#         if (N%i==0) and IsPrime(i) or i==2:
#             print(i)
# N=int(input('Введите натуральное число N'))
# ListPrimeDiv(N)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# list=[4,5,7,2,5,4,6]
# NumOfCoincid=0
# for i in list:
#     for j in list:
#         if j==i:
#             NumOfCoincid=NumOfCoincid+1
#     if NumOfCoincid==1:
#         print(i, end=' ')
#     NumOfCoincid=0

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random
# import pathlib

# k = int(input('Введите коэффициент: '))
# a = int(random.randint(0,100))
# b = int(random.randint(0,100))
# c = int(random.randint(0,100))

# if a != 0:
#     first_part = (str(a) + "x**" + str(k) + " + ")
# else:
#     first_part = (str())

# if b != 0:
#     second_part = (str(b) + "x" + " + ")
# else:
#     second_part = (str())

# if c != 0:
#     third_part = (str(c) + " = 0")
# else:
#     third_part = (str())

# print(f'{first_part}{second_part}{third_part}')
# 35(Доп). Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
