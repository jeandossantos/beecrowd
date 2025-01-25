# -*- coding: utf-8 -*-
n = int(input())

for _ in range(n):
    x, y = map(int, input().split(" "))

    try:
        result = x / y
        print(result)
    except ZeroDivisionError:
        print("divisao impossivel")