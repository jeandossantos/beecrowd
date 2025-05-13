while True:
  # Lê o número de consultas
  K = int(input())

  if K == 0:
      break  # Fim da entrada

  # Lê as coordenadas do ponto divisor
  N, M = map(int, input().split())

  # Processa cada residência
  for _ in range(K):
      X, Y = map(int, input().split())

      if X == N or Y == M:
          print("divisa")
      elif X < N and Y > M:
          print("NO")
      elif X > N and Y > M:
          print("NE")
      elif X > N and Y < M:
          print("SE")
      elif X < N and Y < M:
          print("SO")
