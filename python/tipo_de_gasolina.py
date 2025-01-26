# -*- coding: utf-8 -*-

alcool = 0
gasolina = 0
diesel = 0

while 1:
    opcao = int(input())

    if opcao == 1:
        alcool += 1
    elif opcao == 2:
        gasolina += 1
    elif opcao == 3:
        diesel += 1
    elif opcao == 4:
        print("MUITO OBRIGADO")
        print("Alcool:", alcool)
        print("Gasolina:", gasolina)
        print("Diesel:", diesel)
        break