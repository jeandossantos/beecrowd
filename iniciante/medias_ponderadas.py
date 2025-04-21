# -*- coding: utf-8 -*-

n = int(input())

def calc_media_ponderada(a, b, c):
    PESO_A = 2
    PESO_B = 3
    PESO_C = 5 
    SOMA_DOS_PESOS = PESO_A + PESO_B + PESO_C

    media = ((a * PESO_A) + (b * PESO_B) + (c * PESO_C)) / SOMA_DOS_PESOS

    print(f"{media:.1f}")

for _ in range(n):
    a, b, c = map(float, input().split(" "))

    calc_media_ponderada(a, b, c)