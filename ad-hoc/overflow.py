def main():
  # Leitura do valor máximo N
  N = int(input())

  # Leitura da expressão (P, operador C, Q)
  P, C, Q = input().split()
  P = int(P)
  Q = int(Q)

  # Verifica o tipo da operação
  if C == '+':
      # Soma
      if P + Q > N:
          print("OVERFLOW")
      else:
          print("OK")
  elif C == '*':
      # Multiplicação
      if P * Q > N:
          print("OVERFLOW")
      else:
          print("OK")

# Executa a função principal
main()
