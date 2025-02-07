# -*- coding: utf-8 -*-

valores = list(map(int, input().split(" ")))
a = valores[0]
valores = valores[1:]

n: int = 0

for i in valores:
    if i > 0:
        n = i
        break

somas = []

while n <= 0:
        n = int(input())                

for i in range(0, n):
    somas.append( (a + i))

print(sum(somas))
