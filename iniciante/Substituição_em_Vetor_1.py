# -*- coding: utf-8 -*-

vetor = []

for _ in range(10):
    n = int(input())

    if n is None or n <= 0:
        vetor.append(1)
    else:
        vetor.append(n)

for i in range(len(vetor)):
    print(f"X[{i}] =", vetor[i])
