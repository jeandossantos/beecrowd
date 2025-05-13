# Mapeia os tipos de feedback para os nomes dos responsáveis
responsaveis = {
    "1": "Rolien",
    "2": "Naej",
    "3": "Elehcim",
    "4": "Odranoel"
}

# Lê o número de casos de teste
N = int(input())

for _ in range(N):
    K = int(input())  # Número de feedbacks
    for _ in range(K):
        tipo = input().strip()
        print(responsaveis[tipo])
