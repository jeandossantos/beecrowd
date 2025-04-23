while True:
  n = int(input())  # lê a quantidade de cartas
  if n == 0:
      break  # encerra o programa quando n for 0

  pilha = list(range(1, n + 1))  # inicializa a pilha com cartas de 1 a n
  descartadas = []  # lista para armazenar as cartas descartadas

  # Realiza as operações enquanto houver mais de uma carta na pilha
  while len(pilha) > 1:
      descartadas.append(pilha.pop(0))  # descarta a carta do topo
      pilha.append(pilha.pop(0))  # move a próxima carta para a base

  # A carta remanescente é a única que sobra na pilha
  restante = pilha[0]

  # Imprime os resultados conforme o formato solicitado
  if descartadas:
      print("Discarded cards:", ", ".join(map(str, descartadas)))
  else:
      print("Discarded cards:")
  print("Remaining card:", restante)
