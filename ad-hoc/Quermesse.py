def main():
  teste = 1
  while True:
      # Lê o número de participantes
      N = int(input())

      # Se N for zero, termina o programa
      if N == 0:
          break

      # Lê os ingressos dos participantes
      ingressos = list(map(int, input().split()))

      # Busca o ingresso que é igual à sua posição
      for i in range(N):
          if ingressos[i] == i + 1:  # i + 1 é a posição no teste (1-indexed)
              ganhador = ingressos[i]
              break

      # Imprime o resultado do teste
      print(f"Teste {teste}")
      print(ganhador)
      print()  # Linha em branco após cada teste

      teste += 1

# Executa o programa
main()
