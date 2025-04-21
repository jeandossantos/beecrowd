class FenwickTree:
  def __init__(self, size):
      self.tree = [0] * (size + 2)
      self.size = size + 2

  def update(self, index, value):
      while index < self.size:
          self.tree[index] += value
          index += index & -index

  def query(self, index):
      result = 0
      while index > 0:
          result += self.tree[index]
          index -= index & -index
      return result

def contar_triplas_invertidas(n, arr):
  max_val = n + 1
  esquerda = FenwickTree(max_val)
  direita = FenwickTree(max_val)

  # Preenche direita com a frequência de todos os elementos
  freq = [0] * (max_val)
  for val in arr:
      freq[val] += 1
  for i in range(1, max_val):
      if freq[i]:
          direita.update(i, freq[i])

  total_triplas = 0
  for j in range(n):
      aj = arr[j]
      direita.update(aj, -1)  # Remove aj da direita
      maiores_à_esquerda = esquerda.query(max_val - 1) - esquerda.query(aj)
      menores_à_direita = direita.query(aj - 1)
      total_triplas += maiores_à_esquerda * menores_à_direita
      esquerda.update(aj, 1)  # Adiciona aj na esquerda
  return total_triplas

# Leitura da entrada
n = int(input())
arr = list(map(int, input().split()))
print(contar_triplas_invertidas(n, arr))