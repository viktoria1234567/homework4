#1.Вычислить число c заданной точностью d
# from math import pi

# d =  int(input("Введите количество чисел после запятой для числа Пи: "))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

#2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N =  int(input("Введите натуральное число: "))
# list = []
# i = 2 # первое простое число
# while i <= N:
#     if N % i == 0:
#         list.append(i)
#         N //= i
#         i = 2
#     else:
#         i += 1
# print(list)

#3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# lst = list(map(int, input("Введите числа через пробел: ").split()))
# print(lst)
# new_lst = [ ]
# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)  
#     i=i+1 
# print(new_lst)

#4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# import random


# def write_file(st):
#     with open('file33.txt', 'w') as data:
#         data.write(st)


# def rnd():
#     return random.randint(0,101)


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))