# -*- coding: utf-8 -*-

n = int(input()) + 1

for i in range(2, n): 
    if i % 2 == 0:
        print(f"{i}^2 =", i ** 2)