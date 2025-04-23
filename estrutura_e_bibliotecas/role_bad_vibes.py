def gerar_relatorio():
  # Lê as dimensões da matriz
  N, M = map(int, input().split())

  vida = []
  disciplina = []

  # Lê a matriz e separa os problemas
  for _ in range(N):
      linha = input().split()
      for item in linha:
          criticidade = int(item[0])
          tipo = item[1]

          if tipo == 'V':
              vida.append((criticidade, item))
          else:
              disciplina.append((criticidade, item))

  # Ordena os problemas de vida e disciplina por criticidade (descrescente)
  vida.sort(reverse=True)
  disciplina.sort(reverse=True)

  # Imprime o relatório final
  for _, problema in vida:
      print(problema)
  for _, problema in disciplina:
      print(problema)

# Executa a função
gerar_relatorio()