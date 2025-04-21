# -*- coding: utf-8 -*-

n = int(input())

arr = [n]

for i in range(9):
    arr.append(arr[i] * 2)


for i in range(len(arr)):
    print(f"N[{i}] =", arr[i])