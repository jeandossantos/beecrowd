while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
      break

  servidores = []
  for _ in range(N):
      partes = input().split()
      servidores.append(set(partes[1:]))

  clientes = []
  for _ in range(M):
      partes = input().split()
      clientes.append(set(partes[1:]))

  total_conexoes = 0
  for cliente in clientes:
      conectados = set()
      for idx_servidor, servidor in enumerate(servidores):
          if cliente & servidor:  # interseção não vazia
              conectados.add(idx_servidor)
      total_conexoes += len(conectados)

  print(total_conexoes)
