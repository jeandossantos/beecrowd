def top_category(K):
  # Lista das categorias de colocação
  categories = [1, 3, 5, 10, 25, 50, 100]

  # Encontrar a menor categoria que seja maior ou igual a K
  for category in categories:
      if K <= category:
          return f"Top {category}"

# Entrada
K = int(input())

# Saída
print(top_category(K))
