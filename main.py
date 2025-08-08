MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

AMOUNT_LIMIT = 500
DRAW_LIMIT = 3
balance = 0
extract = ""
draw_times = 0

while True:
    command = input(MENU)

    if command == "d":
        pass

    elif command == "s":
        pass

    elif command == "e":
        pass

    elif command == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")