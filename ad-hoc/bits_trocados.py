def calcular_cedulas(valor):
  cedulas_50 = valor // 50
  valor %= 50

  cedulas_10 = valor // 10
  valor %= 10

  cedulas_5 = valor // 5
  valor %= 5

  cedulas_1 = valor // 1
  valor %= 1

  return cedulas_50, cedulas_10, cedulas_5, cedulas_1

def main():
  teste = 1
  while True:
      # Lê o valor solicitado
      V = int(input())

      # Fim da entrada
      if V == 0:
          break

      # Calcula as cédulas
      I, J, K, L = calcular_cedulas(V)

      # Imprime o resultado do teste
      print(f"Teste {teste}")
      print(f"{I} {J} {K} {L}")
      print()  # Linha em branco após cada teste

      teste += 1

# Executa o programa
main()
