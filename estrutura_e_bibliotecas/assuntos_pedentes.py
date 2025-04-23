def contar_assuntos_pendentes(s):
  pendentes = 0

  for char in s:
      if char == '(':
          pendentes += 1
      elif char == ')':
          if pendentes > 0:
              pendentes -= 1

  if pendentes == 0:
      print("Partiu RU!")
  else:
      print(f"Ainda temos {pendentes} assunto(s) pendente(s)!")

# Leitura da string de entrada
entrada = input().strip()
contar_assuntos_pendentes(entrada)