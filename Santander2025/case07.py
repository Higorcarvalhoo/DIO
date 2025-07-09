from datetime import datetime

# Classe Veiculo com os atributos marca, modelo e ano
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método para verificar se o veículo é antigo
    def verificar_antiguidade(self):
        ano_atual = datetime.now().year
        if ano_atual - self.ano > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"

# Entrada dos dados do veículo
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Criação do objeto e chamada do método
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())
