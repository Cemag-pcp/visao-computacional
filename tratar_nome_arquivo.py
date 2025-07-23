import os
from datetime import datetime

# Caminho da pasta
pasta = r"C:\Users\pcp2\visao\visao-computacional\frames_extraidos"

# Data e hora atual (formato: AAAA-MM-DD_HHMMSS)
data_hora_atual = datetime.now().strftime("%Y-%m-%d_%H%M%S")

# Percorre todos os arquivos da pasta
for nome_arquivo in os.listdir(pasta):
    caminho_antigo = os.path.join(pasta, nome_arquivo)

    # Ignora subpastas e arquivos ocultos
    if not os.path.isfile(caminho_antigo) or nome_arquivo.startswith('.'):
        continue

    novo_nome = f"{data_hora_atual}_{nome_arquivo}"
    caminho_novo = os.path.join(pasta, novo_nome)

    os.rename(caminho_antigo, caminho_novo)
    print(f"Renomeado: {nome_arquivo} -> {novo_nome}")