# Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.

# Сделайте так чтобы эти данные уже никто не смог поменять позже.


a = 0
sets = set()

while a < 10:

	user = int(input("Введите число! "))
	a = a+1
	sets.add(user)
	print(frozenset(sets))

	

