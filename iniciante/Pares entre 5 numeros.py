# -*- coding: utf-8 -*-

pares = []

for _ in range(5):
    n = int(input())

    if n == 0:
        pares.append(n)
        continue

    if n % 2 == 0: pares.append(n)

print(len(pares), "valores pares")
