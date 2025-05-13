while True:
  N = int(input())
  if N == 0:
      break

  mais_antigo = ""
  menor_ano = float('inf')

  for _ in range(N):
      partes = input().split()
      nome = partes[0]
      A = int(partes[1])
      T = int(partes[2])
      ano_envio = A - T

      if ano_envio < menor_ano:
          menor_ano = ano_envio
          mais_antigo = nome

  print(mais_antigo)
