def min_factorial_sum(N):
  # Calcular os fatoriais até N
  factorials = []
  fact = 1
  i = 1
  while fact <= N:
      factorials.append(fact)
      i += 1
      fact *= i  # Calcula o fatorial de i

  # Agora fazemos a soma dos fatoriais com uma abordagem gananciosa
  count = 0
  for f in reversed(factorials):
      while N >= f:
          N -= f
          count += 1
      if N == 0:
          break

  return count

# Entrada
N = int(input())

# Saída
print(min_factorial_sum(N))
