# -*- coding: utf-8 -*-

t = int(input())

n = []

while len(n) < 1000:
    for i in range(t):
        n.append(i)

for i in range(len(n[0:1000])):
    print(f"N[{i}] =", n[i])