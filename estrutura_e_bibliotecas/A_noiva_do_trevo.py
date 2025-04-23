def to_minutos(horario):
  horas, minutos = map(int, horario.split(':'))
  if horas == 23:
      return - (60 - minutos)
  else:
      return minutos

def relatos_verdadeiros():
  P, Q = map(int, input().split())

  relatos = []

  for _ in range(Q):
      H, N = input().split()
      minutos = to_minutos(H)
      if -P <= minutos <= P:
          relatos.append((minutos, N))

  # Ordena por tempo (minutos), mantendo ordem de inserção para horários iguais
  relatos.sort(key=lambda x: x[0])

  for _, nome in relatos:
      print(nome)

# Chamada da função
relatos_verdadeiros()
