# -*- coding: utf-8 -*-

notas = []

while 1:
    n = float(input())

    if n < 0 or n > 10:
        print("nota invalida")
        continue

    notas.append(n)

    if len(notas) == 2: 
        media = sum(notas) / 2
        print("media =", media)
        break