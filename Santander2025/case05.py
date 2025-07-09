# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar os dados dos pacientes com índice de chegada
pacientes = []

# Loop para entrada de dados
for i in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status, i))  # adiciona ordem de chegada

# Função de ordenação com prioridade ajustada
def prioridade(paciente):
    nome, idade, status, chegada = paciente

    if status == "urgente":
        return (0, -idade, chegada)  # prioridade máxima, depois maior idade
    elif idade >= 60:
        return (1, chegada)          # prioridade média
    else:
        return (2, chegada)          # prioridade normal

# Ordenar os pacientes com base na função de prioridade
pacientes_ordenados = sorted(pacientes, key=prioridade)

# Extrair nomes para a saída
nomes_ordenados = [paciente[0] for paciente in pacientes_ordenados]

# Exibir resultado
print("Ordem de Atendimento:", ", ".join(nomes_ordenados))
