# -*- coding: utf-8 -*-

x = int(input())
z = 0

while z <= x:
    z = int(input())

count = 1
sum = x

for i in range(x +1, z):
    count += 1
    sum += i
    
    if sum > z: break

print(count)