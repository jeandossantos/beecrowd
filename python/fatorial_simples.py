# -*- coding: utf-8 -*-
import sys
n = int(input())

if n == 0 or n == 1:
    print(1)
    sys.exit()

sum = n

for i in range(n -1, 0, -1):
    sum *= i

print(sum)