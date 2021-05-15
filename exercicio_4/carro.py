import automovel

carro1 = automovel.Automovel(100, 50, 50)

ans = True
while ans:
    print("""
    1.Combustivel
    2.Autonomia
    3.Abastecer
    4.Fazer Viagem
    5.Sair
    """)
    ans = input("O que deseja fazer? ")
    if ans == "1":
        print(carro1.combustivel())
    elif ans == "2":
        print(carro1.autonomia())
    elif ans == "3":
        print(carro1.abastece(50))
    elif ans == "4":
        carro1.percorre(50)
    elif ans == "-1":
        print("\n Adeus")
    elif ans != "":
        print("\n Escolha inválida. Tente outra vez")
