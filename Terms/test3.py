# Написать программу которая проверит число на несколько критериев:
#
# Чётное ли число?
#
# Делится ли число на 3 без остатка?
#
# Если возвести его в квадрат, больше ли оно 1000?


user = int(input("Введите число: "))

rewenie = user % 2

if rewenie == 0:
    print("Это четное число! ")
else:
    print("Это нечетное число!  ")
