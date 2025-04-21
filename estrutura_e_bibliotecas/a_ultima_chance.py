def is_sorted(s):
  return list(s) == sorted(s)

def check_sequence(m, sequence):
  count = 0
  for i in range(m):
      for j in range(i+1, m):
          lst = list(sequence)
          lst[i], lst[j] = lst[j], lst[i]
          if is_sorted(lst):
              count += 1
          if count > 1:
              return "There aren't the chance."
  return "There are the chance." if count == 1 else "There aren't the chance."

# Leitura da entrada
N = int(input())
for _ in range(N):
  M = int(input())  # Agora lemos M separadamente
  seq = input().strip()  # Lê a sequência em seguida
  print(check_sequence(M, seq))
