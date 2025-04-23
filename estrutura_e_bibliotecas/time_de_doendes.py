def organizar_duendes():
  # Ler o número de duendes
  N = int(input())  # O número de duendes (sempre múltiplo de 3)

  # Lista para armazenar os duendes
  duendes = []

  # Ler os duendes
  for _ in range(N):
      nome, idade = input().split()
      duendes.append((nome, int(idade)))

  # Ordenar os duendes:
  # 1. Ordenar por idade de forma decrescente (inverter a ordem)
  # 2. Em caso de empate na idade, ordenar pelo nome de forma crescente
  duendes.sort(key=lambda x: (-x[1], x[0]))

  # Calcular quantos times serão formados
  times = N // 3

  # Dividir os duendes em times e exibir
  for t in range(times):
      print(f"Time {t + 1}")

      # Atribuir o líder, entregador e piloto de cada time
      lider = duendes[times * 0 + t]      # Primeiro terço para líderes
      entregador = duendes[times * 1 + t]  # Segundo terço para entregadores
      piloto = duendes[times * 2 + t]      # Terceiro terço para pilotos

      # Imprimir as informações de cada duende
      print(f"{lider[0]} {lider[1]}")
      print(f"{entregador[0]} {entregador[1]}")
      print(f"{piloto[0]} {piloto[1]}")

      # Linha em branco após cada time
      print()

# Chamar a função principal
organizar_duendes()