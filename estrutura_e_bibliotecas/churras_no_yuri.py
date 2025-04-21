while True:
  try:
      # Lê o número de peças de carne
      N = int(input())

      if N == 0:
          break

      carnes = []

      # Lê as peças de carne e suas datas de validade
      for _ in range(N):
          carne, validade = input().split()
          validade = int(validade)
          carnes.append((carne, validade))

      # Ordena as carnes pela data de validade
      carnes.sort(key=lambda x: x[1])

      # Imprime os nomes das carnes ordenados
      print(" ".join(carne for carne, _ in carnes))

  except EOFError:
      break
