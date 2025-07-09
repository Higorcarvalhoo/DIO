# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# Loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()
    nome, tema = [parte.strip() for parte in linha.split(',')]

    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(nome)

# Junta tudo em uma única string de saída
saida = ''
for tema, lista in eventos.items():
    saida += f"{tema}: {', '.join(lista)}\n"

# Imprime tudo de uma vez, removendo o último \n com strip()
print(saida.strip())
