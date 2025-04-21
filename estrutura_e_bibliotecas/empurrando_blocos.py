while True:
  H, P, F = map(int, input().split())
  if H == 0 and P == 0 and F == 0:
      break

  # Leitura da matriz
  estoque = [list(map(int, input().split())) for _ in range(H)]

  # Leitura da fila de blocos
  fila = list(map(int, input().split()))

  for bloco in fila:
      colocado = False
      for col in reversed(range(P)):  # da direita pra esquerda
          for lin in reversed(range(H)):  # de baixo pra cima
              if estoque[lin][col] == 0:
                  estoque[lin][col] = bloco
                  colocado = True
                  break
          if colocado:
              break  # vá para o próximo bloco

  # Imprime o estoque final
  for linha in estoque:
      print(' '.join(map(str, linha)))
