from collections import deque
import sys

input = sys.stdin.read
dados = input().split()

N = int(dados[0])
alturas = list(map(int, dados[1:]))

class Node:
    def __init__(self, altura):
        self.altura = altura
        self.esq = None
        self.dir = None

def inserir(raiz, altura):
    if altura < raiz.altura:
        if raiz.esq:
            inserir(raiz.esq, altura)
        else:
            raiz.esq = Node(altura)
    else:
        if raiz.dir:
            inserir(raiz.dir, altura)
        else:
            raiz.dir = Node(altura)

def menores_por_nivel(raiz):
    fila = deque()
    fila.append((raiz, 0))
    niveis = {}

    while fila:
        no, nivel = fila.popleft()
        if nivel not in niveis:
            niveis[nivel] = []
        niveis[nivel].append(no.altura)
        if no.esq:
            fila.append((no.esq, nivel + 1))
        if no.dir:
            fila.append((no.dir, nivel + 1))

    for nivel in sorted(niveis.keys()):
        print(f"{nivel} {min(niveis[nivel])}")

raiz = Node(alturas[0])
for altura in alturas[1:]:
    inserir(raiz, altura)

menores_por_nivel(raiz)
