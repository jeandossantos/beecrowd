def main():
  # Leitura do número de divisões
  N = int(input())

  # Leitura da lista de divisões
  divisoes = list(map(int, input().split()))

  # Variável para armazenar o número total de pedaços armazenados
  pedaços_armazenados = 0

  # Para cada divisão, calculamos os pedaços armazenados
  for i in divisoes:
      pedaços_armazenados += i - 1

  # Imprime o resultado
  print(pedaços_armazenados)

# Chama a função principal
main()
