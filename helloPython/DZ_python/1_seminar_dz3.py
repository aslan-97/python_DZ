# напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

x = float(input("введите X: "))
y = float(input("введите Y: "))
x != 0
y != 0
if 1 < x and 1 < y:
    print("1 четверть")
elif x < -1 and 1 < y:
    print("2 четверть")
elif x < -1 and y < -1:
    print("3 четверть")
elif 1 < x and y < -1:
    print("4 четверть")
