# Lê M e N
M, N = map(int, input().split())

# Lê o dicionário de palavras
hay_points = {}
for _ in range(M):
    palavra, valor = input().split()
    hay_points[palavra] = int(valor)

# Processa cada descrição de cargo
for _ in range(N):
    total = 0
    while True:
        linha = input().strip()
        if linha == ".":
            break
        palavras = linha.split()
        for palavra in palavras:
            total += hay_points.get(palavra, 0)
    print(total)
