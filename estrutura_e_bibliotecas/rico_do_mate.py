 # Leitura dos dados
N, L, Q = input().split()
N = int(N)
L = float(L)
Q = float(Q)

nomes = input().split()

# Inicializa variáveis
i = 0
while L > 0:
    nome = nomes[i % N]
    if L >= Q:
        ultima_quantidade = Q
        L -= Q
    else:
        ultima_quantidade = L
        L = 0
    i += 1

# i foi incrementado após a última pessoa, então voltamos um
rico = nomes[(i - 1) % N]
print(f"{rico} {ultima_quantidade:.1f}")
