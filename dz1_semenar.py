# Задача 1: Найдите сумму цифр трехзначного числа.

# num = int(input('введите число: '))
# sum = 0
# while num!=0:
#     s =  num % 10
#     sum +=s
#     num = num //10
# print(sum)



# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input("введите общее количество журавликов: "))
# cat = s / 2
# peti = cat / 2
# serezha = cat / 2
# print(f'Катя ={cat}')
# print(f'Петя={peti}')
# print(f'Сережа={serezha}')



# Задача 3: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# num = int(input('введите номер билетика: '))
# sum = num // 1000
# len = num % 1000
# m = 0
# n = 0
# while sum!=0:
#     s =  sum % 10
#     m +=s
#     sum = sum //10

# while len!=0:
#     s =  len % 10
#     n +=s
#     len = len //10

# if m == n:
#     print('ваш билет счастливый')
# else:
#     print('ваш билет не счастливый')

