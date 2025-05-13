while True:
  N = int(input())
  if N == 0:
      break

  tempos = list(map(int, input().split()))
  tempo_total = 0
  inicio = tempos[0]
  fim = inicio + 10

  for t in tempos[1:]:
      if t > fim:
          tempo_total += fim - inicio
          inicio = t
          fim = t + 10
      else:
          fim = max(fim, t + 10)

  tempo_total += fim - inicio
  print(tempo_total)
