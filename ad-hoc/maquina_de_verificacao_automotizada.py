# -*- coding: utf-8 -*-

x = list(map(int, input().split()))
y = list(map(int, input().split()))

compatível = all(xi + yi == 1 for xi, yi in zip(x, y))

print("Y" if compatível else "N")