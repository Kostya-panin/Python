# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
# def sumdigit(number):
#     number1 = number
#     sumdigit = 0
#     while (number1 > 0):
#         digitN = number1 % 10
#         number1 = number1 / 10
#         sumdigit = sumdigit + digitN
#     return int(sumdigit)
# print("Введите число")
# number=int(input())
# print(sumdigit(number))

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
# 5! = 120
# number=5
# def faktorial(number):
#     i=1
#     a=1
#     while (i<number):
#         i=i+1
#         a=a*i
#     print(a)
# print('Введите число')
# number=int(input()) 
# faktorial(number)


# Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение второго по величине элемента в этой последовательности,
#  то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
# Пример:
# 1 7 9 0
# Вывод: 7
#Способ1
# def secondmax(array):
#     N=len(array)
#     for i in range(N-1):
#         for j in range(N-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#     return array[-2]
# a=[7,4,8,3,9,0]
# print(secondmax(a))   
# #Способ2
# def secondMaximum(array):
#     array=sorted(array)
#     return array[-2]
# array=[4,5,6,7,10,4,8]
# print(secondMaximum(array))

# Дополнительно:
# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть копеек отбрасывается.
# Требуется определить: через сколько лет вклад составит не менее Y рублей.
# Пример:
# 100 10 200
# Вывод: 8

# def vklad(X,P,Y):
#     i=0
#     while Y>X:
#         X=int(X+((X/100)*P))/1
#         i=i+1
#     return i
# print("Введите размер вклада,процентов на которые будет увеличиваться вклад и какую сумму вы хотите заработать")
# X,P,Y=map(int, input().split())
# print("Нужную сумму вы на копите за",(vklad(X,P,Y)),"лет")


