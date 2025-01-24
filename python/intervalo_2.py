# -*- coding: utf-8 -*-

x = int(input())

in_range = []
out_range = []

for _ in range(x):
    n = int(input())

    if n >= 10 and n <= 20: 
        in_range.append(n)

    elif n <= 10 or n >= 20:
        out_range.append(n)

print(len(in_range), "in")
print(len(out_range), "out")