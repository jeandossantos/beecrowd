n = int(input())
soma = []

def troca_valores(x, y):
  if x > y:
    return y, x
  return x, y

for _ in range(n):
  x, y = map(int, input().split(" "))
  x, y = troca_valores(x, y)    

  if (y - x) == 0:
    soma.append(0)
    continue

  acc = 0

  for n in range(x + 1, y):
    if n % 2 == 1:
      acc += n

  soma.append(acc)

[print(s) for s in soma]