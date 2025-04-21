# -*- coding: utf-8 -*-
idades = []

while 1:
    idade = int(input())
    if idade < 0:
        break

    idades.append(idade)

print(f"{sum(idades) / len(idades):.2f}")