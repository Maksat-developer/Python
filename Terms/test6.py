# Напишите условие, которое выводит отрицательные числа

user = int(input("Введите любое число! "))

if user < 0:
    print("Это отрицательное число! ")
elif user == 0:
    print("Это нейтральное число")
else:
    print("Это положительное число! ")

