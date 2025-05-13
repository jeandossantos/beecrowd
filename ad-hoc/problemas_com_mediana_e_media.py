def mediana(a, b, c):
  return sorted([a, b, c])[1]

while True:
  A, B = map(int, input().split())
  if A == 0 and B == 0:
      break

  candidatos = []
  for med in [A, B]:
      C = 3 * med - A - B
      if mediana(A, B, C) == (A + B + C) // 3:
          candidatos.append(C)

  print(min(candidatos))
