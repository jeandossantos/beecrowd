# -*- coding: utf-8 -*-

x = int(input())
impares = []

while len(impares) < 6:
  x += 1

  if x % 2 != 0:
    impares.append(x)
    print(x)
