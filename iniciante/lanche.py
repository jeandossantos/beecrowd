# -*- coding: utf-8 -*-

produtos = (
    (1, 4),
    (2, 4.5),
    (3, 5),
    (4, 2),
    (5, 1.5)
    )

cod, qtd = map(int, input().split(" "))

total = 0

for p in produtos:
    if p[0] == cod:
        total = p[1] * qtd
        break

print(f"Total: R$ {total:.2f}")