"""
Задание 1. Новые списки
Даны три списка:
1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
Напишите код, который создаёт три новых списка. Вот их содержимое:
1. Каждое число из списка floats возводится в третью степень и округляется
до трёх знаков после запятой.
2. Из списка names берутся только имена минимум из пяти букв.
3. Из списка numbers берётся произведение всех чисел.

"""
import math
from functools import reduce


floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

map_rez = list(map(lambda x: round(x**3, 3), floats))
print(map_rez)
filter_rez = list(filter(lambda x: len(x) >= 5, names))
print(filter_rez)
reduce_rez = reduce(lambda x1, x2: x1 * x2, numbers)
print(reduce_rez)