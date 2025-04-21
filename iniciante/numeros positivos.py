# -*- coding: utf-8 -*-

positivos = []

for _ in range(6):
    n = float(input())

    if n > 0: positivos.append(n)

print(len(positivos), "valores positivos")
