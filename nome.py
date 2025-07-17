import os

# Pasta alvo
pasta = r'C:\Users\TI DEV\visao-computacional\datasets\dataset\labels\val'

# Lista todos os arquivos da pasta
for nome_antigo in os.listdir(pasta):
    caminho_antigo = os.path.join(pasta, nome_antigo)

    # Ignora pastas
    if not os.path.isfile(caminho_antigo):
        continue

    # Verifica se já tem prefixo
    if nome_antigo.startswith('5_'):
        continue

    # Novo nome com prefixo '5_'
    nome_novo = f'5_{nome_antigo}'
    caminho_novo = os.path.join(pasta, nome_novo)

    # Renomeia
    os.rename(caminho_antigo, caminho_novo)

print("? Renomeação concluída com prefixo '5_'")
