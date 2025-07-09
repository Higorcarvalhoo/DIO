class Pedido:
    def __init__(self):
        self.itens = []  # Lista de preços
    
    # Método para adicionar um item ao pedido
    def adicionar_item(self, preco):
        self.itens.append(preco)

    # Método para calcular o valor total do pedido
    def calcular_total(self):
        return sum(self.itens)

# Lê a quantidade de pedidos
quantidade_pedidos = int(input().strip())

# Cria um novo pedido
pedido = Pedido()

# Lê e processa cada item
for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)  # separa nome e preço
    pedido.adicionar_item(float(preco))  # adiciona apenas o valor

# Exibe o total com 2 casas decimais
print(f"{pedido.calcular_total():.2f}")
