usuarios = {}
cpf_usuarios = []
agencia = "0001"
contador_contas = 1

def criar_usuario():
    while True:
        try:
            cpf = int(input("Digite seu CPF: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um CPF válido.")
            continue

        if cpf in cpf_usuarios:
            print("CPF já cadastrado.")
            continue
        else:
            cpf_usuarios.append(cpf)
            print("CPF cadastrado com sucesso.")
            break

    nome = input("Informe seu nome completo: ")

    while True:
        try:
            dia = int(input("Informe o dia do seu nascimento: "))
            if 1 <= dia <= 31:
                break
            else:
                print("Dia inválido.")
        except ValueError:
            print("Entrada inválida.")

    while True:
        try:
            mes = int(input("Informe o mês do seu nascimento: "))
            if 1 <= mes <= 12:
                break
            else:
                print("Mês inválido.")
        except ValueError:
            print("Entrada inválida.")

    while True:
        try:
            ano = int(input("Informe o ano do seu nascimento: "))
            if 1900 <= ano <= 2025:
                break
            else:
                print("Ano inválido.")
        except ValueError:
            print("Entrada inválida.")

    nascimento = f"{dia:02d}/{mes:02d}/{ano}"

    usuarios[cpf] = {
        "nome": nome,
        "nascimento": nascimento,
        "enderecos": [],
        "contas": []
    }

def criar_conta():
    global contador_contas 
    try:
        cpf = int(input("Digite seu CPF: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if cpf not in cpf_usuarios:
        print("CPF não localizado.")
        return

    nova_conta = {
        "agencia": agencia,
        "numero": f"{contador_contas:04d}",
        "saldo": 0,
        "historico": []
    }

    usuarios[cpf]["contas"].append(nova_conta)
    contador_contas += 1 
    print("Conta criada com sucesso!")

# ---------------------- Movimentações --------------------------

limite = 500
LIMITESAQUE = 3

def menu_operacoes(conta):
    menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""
    while True:
        opcao = input(menu)
        if opcao == "1":
            depositar(conta)
        elif opcao == "2":
            sacar(conta)
        elif opcao == "3":
            mostrar_extrato(conta)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def depositar(conta):
    try:
        valor = float(input("Valor para depósito: "))
        if valor <= 0:
            print("Valor inválido.")
            return
        conta["saldo"] += valor
        conta["historico"].append(f"Depósito de R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    except ValueError:
        print("Entrada inválida.")

def sacar(conta):
    try:
        valor = float(input("Valor para saque: "))
    except ValueError:
        print("Entrada inválida.")
        return

    saques_realizados = [op for op in conta["historico"] if "Saque" in op]

    if valor <= 0:
        print("Valor inválido.")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente.")
    elif valor > limite or len(saques_realizados) >= LIMITESAQUE:
        print("Limite de saque excedido.")
    else:
        conta["saldo"] -= valor
        conta["historico"].append(f"Saque de R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

def mostrar_extrato(conta):
    print("\n=== EXTRATO ===")
    if not conta["historico"]:
        print("Nenhuma movimentação.")
    else:
        for operacao in conta["historico"]:
            print(operacao)
    print(f"Saldo atual: R${conta['saldo']:.2f}")
    print("================\n")

def acessar_conta():
    try:
        cpf = int(input("Digite seu CPF: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if cpf not in usuarios:
        print("CPF não encontrado.")
        return

    contas = usuarios[cpf]["contas"]
    if not contas:
        print("Usuário não possui contas.")
        return

    print("Contas disponíveis:")
    for i, conta in enumerate(contas):
        print(f"[{i}] Conta {conta['numero']} | Agência {conta['agencia']}")

    try:
        escolha = int(input("Escolha uma conta para acessar: "))
        conta_escolhida = contas[escolha]
        menu_operacoes(conta_escolhida)
    except (IndexError, ValueError):
        print("Conta inválida.")

# ---------------------- MENU GERAL --------------------------

menu_geral = """
=== MENU PRINCIPAL ===
[1] Cadastrar novo usuário
[2] Criar nova conta
[3] Acessar conta bancária
[0] Sair
"""

while True:
    opcao = input(menu_geral)
    if opcao == "1":
        criar_usuario()
    elif opcao == "2":
        criar_conta()
    elif opcao == "3":
        acessar_conta()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
