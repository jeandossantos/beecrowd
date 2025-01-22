# -*- coding: utf-8 -*-

KM_POR_L = 12

tempo_gasto = int(input())
velocidade_media = int(input())

distancia_percorrida = tempo_gasto * velocidade_media

litros_necessarios = distancia_percorrida / KM_POR_L

print(f"{litros_necessarios:.3f}")