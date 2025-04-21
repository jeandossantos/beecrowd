# -*- coding: utf-8 -*-

grenais = 0
inter_vitorias = 0
gremio_vitorias = 0
empates = 0

while 1:
    grenais += 1
    gols_inter, gols_gremio = map(int, input().split(" "))
    has_new_grenal = int(input("Novo grenal (1-sim 2-nao)\n"))

    if gols_inter > gols_gremio:
        inter_vitorias += 1
    elif gols_inter < gols_gremio:
        gremio_vitorias += 1
    else:
        empates += 1

    if has_new_grenal == 2:
        print(grenais, "grenais")
        print(f"Inter:{inter_vitorias}")
        print(f"Gremio:{gremio_vitorias}")
        print(f"Empates:{empates}")

        if inter_vitorias > gremio_vitorias:
            print("Inter venceu mais")
            break

        print("Gremio venceu mais")
        break
