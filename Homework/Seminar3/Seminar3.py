# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list=[1,2,3,4,5]
# i=0
# a=0
# for i in list:
#     if i%2==0:
#         a=a+i
# print(a)    

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list=[1,2,3,4,3,6,5,6]
# def multiplyStartEnd(list):
#     j=len(list)-1
#     m=1
#     for i in list:
#         if j>=(len(list)/2):
#             m=i*(list[j])
#             j=j-1
#             print('position J',j)
#             print(m)
# multiplyStartEnd(list)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list=[1.6, 9.3, 1.5 ,4.7, 3.67,2.132]
# def divmaxmin(list):
#     min=list[0]
#     max=0
#     for i in list:
#         if i%1>max:
#             max=i%1
#         elif i%1<min:
#             min=i%1
#     return max-min        
# print(divmaxmin(list))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# from ast import List
# a=int(input('Слышь введи!!!!'))
# i=0
# string: str = ""
# while a>0:
#     b=a%2
#     a=a//2
#     string+=str(b)
# string=''.join(reversed(string))
# print(string)


