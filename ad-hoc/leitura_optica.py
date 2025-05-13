while True:
  N = int(input())
  if N == 0:
      break

  for _ in range(N):
      valores = list(map(int, input().split()))
      marcadas = [i for i, v in enumerate(valores) if v <= 127]

      if len(marcadas) == 1:
          print(chr(ord('A') + marcadas[0]))
      else:
          print('*')
