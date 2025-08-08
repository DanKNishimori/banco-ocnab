MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

AMOUNT_LIMIT = 500
DRAW_LIMIT = 3
balance = 0
statement = []
draw_times = 0

while True:
    command = input(MENU)

    if command == "d":
        value = float(input("Informe o valor do depósito: "))
        if value <= 0:
            print("valor insuficiente para ser depósitado.")
            continue
        balance += value
        statement.append(f"Depósito: R$ {value:.2f}")

    elif command == "s":
        if draw_times >= DRAW_LIMIT:
            print("Limite de saques diário exedido.")
            continue

        value = float(input("Informe o valor ser sacado: "))
        if 0 > value > 500:
            print("Valor inválido.")
            continue
        elif value <= balance:
            draw_times += 1
            balance -= value
            statement.append(f"Saque: R$ {value:.2f}")
        else:
            print("Saldo insuficiente.")
            continue

    elif command == "e":
        for s in statement:
            print(s)

    elif command == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")