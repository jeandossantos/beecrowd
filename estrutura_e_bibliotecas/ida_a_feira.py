def calcular_valor():
  # Leitura do número de casos de teste
  N = int(input())

  # Para cada caso de teste
  for _ in range(N):
      # Leitura do número de produtos disponíveis na feira
      M = int(input())

      # Dicionário para armazenar os produtos e seus preços
      produtos = {}

      # Leitura dos produtos e preços
      for _ in range(M):
          nome, preco = input().split()
          preco = float(preco)
          produtos[nome] = preco

      # Leitura do número de produtos que Dona Parcinova quer comprar
      P = int(input())

      # Inicializa o valor total
      total = 0

      # Leitura dos produtos desejados e cálculo do total
      for _ in range(P):
          nome, quantidade = input().split()
          quantidade = int(quantidade)
          total += produtos[nome] * quantidade

      # Exibe o resultado formatado com 2 casas decimais
      print(f"R$ {total:.2f}")

# Chama a função para processar os casos de teste
calcular_valor()
