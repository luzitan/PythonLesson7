"""Задача 1: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке

Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод:
Парам пам-пам
"""

n = input()
n = n.split()
count = []
for j in range(len(n)):
    c = 0
    for i in range(len(n[j])):
        if n[j][i] in ("а", "у", "е", "о", "и", "я", "ю", "ы", "э", "ё"):
            c += 1
    count.append(c)
count = set(count)
if len(count) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")