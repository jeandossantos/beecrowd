# -*- coding: utf-8 -*-

x = int(input())
impares = []

while len(impares) < 6:

  if x % 2 != 0: 
    impares.append(x)
    print(x)

  x += 1