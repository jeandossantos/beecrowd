# -*- coding: utf-8 -*-

pares = []
positivos = []
negativos = []
impares = []

for _ in range(5):
    n = int(input())

    if n % 2 == 0: pares.append(n)
    if n > 0: positivos.append(n)
    if n < 0: negativos.append(n)

    if n % 2 != 0: impares.append(n)

print(f"{len(pares)} valor(es) par(es)")
print(f"{len(impares)} valor(es) impar(es)")
print(f"{len(positivos)} valor(es) positivo(s)")
print(f"{len(negativos)} valor(es) negativo(s)")