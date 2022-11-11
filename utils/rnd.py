import random as rnd


# Рандомный счет
# Шанс прохождения скила 50%, максимальный шанс прохождения = 100%, минимальный = 0%
#   if rnd_calc(50, 100):
#       print("Успех!")
#   else:
#       print("Провал!")
# return: boolean true если value > рандом который там выскочил, false во всех остальных случаях
def rnd_calc(value: int, maximal: int) -> bool:
    return value > rnd_get_minmax(0, maximal)


# Случайная калькуляция - перегрузка вышеописанной функции, на делает все то же что и вышеописанная но с границей 100%
# Если мы считаем рандом в пределах от 0 до 100, то используем всегда эту функцию
# Если шанс сложный (где 1.000.000 = 100% то берём вышеописанную функцию)
# Example:
#   if rnd_calc(33):
#       print("Успех!")
#   else:
#       print("Провал!")
def rnd_calc(value: int) -> bool:
    return rnd_calc(value, 100)


# Случайное получение числа в радиусе от 0 до bound аргумента
# Example:
#   var = rnd_get(123123)
#   print(var) // выведет случайное число от 0 до 123123
# Return: случайное число до указанной границы (аргумент=граница)
def rnd_get(bound: int):
    return rnd_get_minmax(0, bound)


# Случайное получение числа в радиусе от minimal до maximal аргументов
# Example:
#   var = rnd_get_minmax(-123123, 123123)
#   print(var) // выведет случайное число от -123123 до 123123
# Return: случайное число от указанной минимальной границы minimal и до указанной максимум границы maximal(аргументы=границы)
def rnd_get_minmax(minimal: int, maximal: int):
    return rnd.randint(minimal, maximal)


# Случайное получение элемента из list
# Example:
#   l = list("qwerty")
#   var = rnd_get(l)
#   в данном случае var = одной из букв "qwerty" которые лежат в листе, может вернуть q,y,t,w,e,r и т.д.
# Return: случайный элемент из списка
def rnd_get(collection: list):
    size: int = len(collection)
    index = rnd_get_minmax(1, size - 1)
    return collection[index]
