T = int(input())

for _ in range(T):
    M = int(input())
    notas = list(map(int, input().split()))

    ordenado = sorted(notas, reverse=True)

    iguais = 0
    for original, novo in zip(notas, ordenado):
        if original == novo:
            iguais += 1

    print(iguais)
