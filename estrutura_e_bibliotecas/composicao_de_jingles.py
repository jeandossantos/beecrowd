# Dicionário com durações das notas
duracoes = {
    'W': 1,
    'H': 1/2,
    'Q': 1/4,
    'E': 1/8,
    'S': 1/16,
    'T': 1/32,
    'X': 1/64
}

while True:
    linha = input().strip()
    if linha == "*":
        break

    compassos = linha.strip("/").split("/")
    corretos = 0

    for compasso in compassos:
        duracao_total = sum(duracoes.get(nota, 0) for nota in compasso)
        if abs(duracao_total - 1) < 1e-6:
            corretos += 1

    print(corretos)
