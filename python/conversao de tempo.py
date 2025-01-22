# -*- coding: utf-8 -*-

tempo = int(input()) # tempo de duração em segundos um evento

horas = tempo // 3600
tempo = tempo % 3600
minutos = tempo // 60
tempo = tempo % 60
segundos = tempo

print(f"{horas}:{minutos}:{segundos}")