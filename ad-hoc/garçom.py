# Leitura do número de bandejas
N = int(input())

# Inicialização do contador de copos quebrados
total_quebrado = 0

# Leitura dos dados das bandejas
for _ in range(N):
    L, C = map(int, input().split())  # L -> latas, C -> copos
    if L > C:  # Se o número de latas for maior que o número de copos
        total_quebrado += C  # O garçom quebra todos os copos

# Imprimir o total de copos quebrados
print(total_quebrado)
