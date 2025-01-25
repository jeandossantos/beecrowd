# -*- coding: utf-8 -*-

while(True):
    x, y = map(int, input().split(" "))

    if x == y: break
        
    print("Decrescente") if x > y else print("Crescente")
