# Спросить у пользователя его год рождения,вычислить
# его возраст, если  возраст больше или равно 18 вывести сообщение "Совершеннолетний",
# если меньше или равно 4 вывести "Ребенок"
# иначе "Несовершеннолетий"

from pprint import pprint as pp

user = int(input("Введите год своего рождения! "))
years = 2021

if years - user >= 18:
    pp("Совершеннолетний")
elif years - user <= 4:
    pp("Ребенок")
else:
    pp("Несовершеннолетий")

