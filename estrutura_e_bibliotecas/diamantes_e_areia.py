N = int(input())  # número de casos de teste

for _ in range(N):
    linha = input()
    pilha = []
    diamantes = 0

    for char in linha:
        if char == '<':
            pilha.append('<')
        elif char == '>':
            if pilha:
                pilha.pop()
                diamantes += 1

    print(diamantes)
