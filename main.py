# 1 1 1
# 1 2 2
# 2 4 8
# 2 5 9
# 3 9 27
# 3 10 28
# 4 16 64
# 4 17 65
# 5 25 125
# 5 26 126

n = int(input())

for i in range(1, n + 1):
    print(i, i * i, i ** 3)
    print(i,(i * i) + 1,(i ** 3) + 1)
