"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""
# def degree(a, n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return a
#     return degree(a, n - 1) * a

# a = int(input('число '))
# n = int(input('степень '))
# print(degree(a,n))




"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
2 2
4
"""

# def sum(a,b):
#     if b == 0:
#         return(a)
#     else:
#         if b > 0:
#             return(sum(a +1, b - 1))
#         else:
#             return(sum(a - 1 , b + 1))
# a = int(input())
# b = int(input())
# print(sum(a,b))



