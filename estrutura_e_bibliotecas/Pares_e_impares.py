# Função principal que vai organizar os números conforme o critério especificado
def ordenar_numeros():
    # Lê o número de entradas
    N = int(input())

    # Inicializa listas para pares e ímpares
    pares = []
    impares = []

    # Lê cada número e classifica como par ou ímpar
    for _ in range(N):
        num = int(input())
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    # Ordena os pares em ordem crescente
    pares.sort()

    # Ordena os ímpares em ordem decrescente
    impares.sort(reverse=True)

    # Imprime os números pares
    for numero in pares:
        print(numero)

    # Imprime os números ímpares
    for numero in impares:
        print(numero)

# Chama a função principal para rodar o programa
ordenar_numeros()
