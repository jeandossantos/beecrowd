from collections import defaultdict

def dfs(no, visitado, grafo):
    visitado[no] = True
    for vizinho in grafo[no]:
        if not visitado[vizinho]:
            dfs(vizinho, visitado, grafo)

# Entrada
n, l = map(int, input().split())  # Número de segmentos e ligações
grafo = defaultdict(list)

# Construção do grafo
for _ in range(l):
    x, y = map(int, input().split())
    grafo[x].append(y)
    grafo[y].append(x)

# Verificar conectividade
visitado = [False] * (n + 1)  # Vetor de visitados (do 1 ao N)
dfs(1, visitado, grafo)       # Inicia a DFS a partir do primeiro segmento

# Checar se todos os segmentos foram visitados
if all(visitado[1:]):
    print("COMPLETO")
else:
    print("INCOMPLETO")