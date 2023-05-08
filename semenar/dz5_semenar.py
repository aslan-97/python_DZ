# Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.

# number_A = int(input("enter A: "))
# number_B = int(input("enter B: "))
# def sum_numbers(a, b):
#     count = a**b
#     if number_B == 0:
#         return 1 
#     if number_B < 0:
#         return 1
#     return count 
# h = sum_numbers(number_A, number_B)
# print(h)


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# a = int(input("enter A: "))
# b = int(input("enter B: "))
# def summa(a, b):
#     a += 1
#     b -= 1
#     if b > 0:
#         return summa(a, b)
#     else:
#         return a
# print (summa(a, b))