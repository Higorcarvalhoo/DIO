
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""
menuDeposito = """
[1] Novo Deposito 
[2] Consultar Extrato Detalhado
[3] Voltar
[0] Finalizar sessão 
"""
menuExtrato="""
[1] Voltar
[2] Finalizar sessão  
"""

saldo = []
historicoSaque =[]
limite = 500
numeroSaques = 0
LIMITESAQUE= 3
total =(sum(saldo))

while True:
    opcaoMenu = input(menu)
    if opcaoMenu == '1':
        #Depositar
        print('Deposito selecionado com sucesso!')
        deposito = float(input("Qual o valor sera depositado? "))
        if deposito <=0:
            print('Por gentileza informar um valor valido!')
        else:
            print(f'Deposito de : R${deposito:.2f}, realizado com sucesso !')
            saldo.append(deposito)
        while True:
            opcaoDeposito = input(menuDeposito)
            #Novo Deposito
            if opcaoDeposito == '1':
                print('Deposito selecionado com sucesso!')
                deposito = float(input('Qual o valor sera depositado? '))
                if deposito <= 0 :
                    print('Por gentileza informar um valor valido!')
                else:
                    print(f'Deposito de : R${deposito:.2f}, realizado com sucesso !')
                    saldo.append(deposito)
            #Consultar Extrato Detalhado
            if opcaoDeposito == '2':
                for elemento in saldo:
                    print(f'Movimentação de R${elemento:.2f}')
                total =(sum(saldo))
                print(f'Seu saldo atual e de R${total:.2f}')
                while True:
                    opcaoExtrato = input(menuExtrato)
                    if opcaoExtrato == '1':
                        break
                    if opcaoExtrato == '2':
                        print('Desligando...')
                        exit()                     
            #Voltar
            if opcaoDeposito == '3':
                opcaoMenu = input(menu)
                break
            #Sair
            if opcaoDeposito == '0':
                print('Desligando...')
                exit()
    if opcaoMenu == '2':
        #Sacar
        print('Saque selecionado com sucesso!')
        saque = float(input("Qual o valor deseja sacar? "))
        numeroSaques = len(historicoSaque)
        if saque <= 0:
            print("Erro: Valor invalido.")
        elif saque > total:
            print("Voce não possui saldo suficiente para realizar o saque")
        elif  saque > limite or numeroSaques >= LIMITESAQUE:
            print('Limite de Saque atingido , entre em contato com seu gerente!')
        else:
            saque = saque*-1
            saldo.append(saque)
            total =(sum(saldo))
            print(f'Saque de R${abs(saque):.2f},Realizado com sucesso.\nSeu Saldo atual e de R${total:.2f}')
            historicoSaque.append(saque)
    if opcaoMenu == '3':
        #Extrato
        for elemento in saldo:
            print(f'Movimentação de R${elemento:.2f}')
        total =(sum(saldo))
        print(f'Seu saldo atual e de R${total:.2f}')
    if opcaoMenu == '0':  
        #Sair 
        print('Desligando...')
        exit()