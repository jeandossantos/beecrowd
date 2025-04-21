
N = int(input())
traducao = {}


for _ in range(N):
    lingua = input().strip()
    mensagem = input().strip()
    traducao[lingua] = mensagem


M = int(input())
etiquetas = []


for _ in range(M):
    nome = input().strip()
    lingua = input().strip()
    etiquetas.append((nome, traducao[lingua]))


for nome, mensagem in etiquetas:
    print(nome)
    print(mensagem)
    print()
