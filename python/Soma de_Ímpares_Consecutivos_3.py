# -*- coding: utf-8 -*-

n = int(input())

for _ in range(n):
    x, y = map(int, input().split(" "))

    valores = []

    while len(valores) < y:
        if x % 2 != 0:
            valores.append(x)

        x += 1

    print(sum(valores))