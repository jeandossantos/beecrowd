while True:
  N = int(input())
  if N == 0:
      break

  pontos_1 = 0
  pontos_2 = 0

  for _ in range(N):
      A, B = map(int, input().split())
      if A > B:
          pontos_1 += 1
      elif B > A:
          pontos_2 += 1
      # Se forem iguais, ninguém pontua

  print(f"{pontos_1} {pontos_2}")
