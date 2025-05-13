while True:
  entrada = input().strip()
  A, B, C = map(int, entrada.split())

  if A == 0 and B == 0 and C == 0:
      break

  volume = A * B * C
  aresta_cubo = int(round(volume ** (1/3)))  # Arredondamos antes de truncar para compensar erros de ponto flutuante

  # Verifica se arredondamos para cima indevidamente
  while aresta_cubo ** 3 > volume:
      aresta_cubo -= 1
  while (aresta_cubo + 1) ** 3 <= volume:
      aresta_cubo += 1

  print(aresta_cubo)
