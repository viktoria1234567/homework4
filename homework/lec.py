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