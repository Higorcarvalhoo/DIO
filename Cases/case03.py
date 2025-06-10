def calcular_saldo(transacoes):
    saldo = 0

    # Itera sobre cada transação e soma ao saldo
    for transacao in transacoes:
        saldo += transacao

    # Retorna o saldo formatado com ponto como separador decimal
    return f"Saldo: R$ {saldo:.2f}"


# Entrada do usuário
entrada_usuario = input("Digite as transações (ex: [100, -50, 200]): ")

# Limpa a entrada e transforma em lista de floats
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")
transacoes = [float(valor) for valor in entrada_usuario.split(",") if valor]

# Calcula e imprime o saldo
resultado = calcular_saldo(transacoes)
print(resultado)
