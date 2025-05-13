def main():
  # Lê os valores de C, P, e F
  C, P, F = map(int, input().split())

  # Calcula o número total de folhas necessárias
  folhas_necessarias = C * F

  # Verifica se as folhas compradas são suficientes
  if P >= folhas_necessarias:
      print('S')
  else:
      print('N')

# Executa a função principal
main()
