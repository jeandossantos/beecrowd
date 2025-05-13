# -*- coding: utf-8 -*-

import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    linhas = n - 2
    colunas = m - 2
    sonares = math.ceil(linhas / 3) * math.ceil(colunas / 3)
    print(sonares)
