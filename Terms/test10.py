# Спросить у пользователя его возраст,
# если значение больше или равно 18 вывести сообщение "Совершеннолетний",
# если меньше или равно 4 вывести "Ребенок" иначе "Несовершеннолетий"

from pprint import pprint as pp

user = int(input("Сколько вам лет? "))

if user >= 18:
    pp("Совершеннолетний")

elif user <= 4:
    pp("Ребенок")

else:
    pp("Несовершеннолетий")