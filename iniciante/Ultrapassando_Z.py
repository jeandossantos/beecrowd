# -*- coding: utf-8 -*-

x = int(input())
n = 0

while n <= x:
    n = int(input())

count = 1
sum = x

for i in range(x +1, n):
    count += 1
    sum += i

    if sum > n: break

print(count)