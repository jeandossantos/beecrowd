def hex_to_ascii():
  # Lê o número de caracteres
  n = int(input())

  # Lê os valores hexadecimais
  hex_values = input().split()

  # Converte os hexadecimais para caracteres e imprime a mensagem
  message = ''.join(chr(int(hex_value, 16)) for hex_value in hex_values)

  print(message)

# Chama a função
hex_to_ascii()
