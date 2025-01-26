# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

if x > y: 
    x, y = y, x

acc = 0

for n in range(x, y + 1):
    if n % 13 != 0:
        acc += n

print(acc)

