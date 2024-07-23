import os
import pandas as pd

# Caminho para o diretório com os arquivos de anotações
diretorio_anotacoes = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Annotations'

# Lista para armazenar os dados de todos os arquivos
dados = []

# Percorre todos os arquivos no diretório de anotações
for arquivo in os.listdir(diretorio_anotacoes):
    caminho_arquivo = os.path.join(diretorio_anotacoes, arquivo)
    if os.path.isfile(caminho_arquivo) and arquivo.endswith('.csv'):
        # Carrega o arquivo CSV como DataFrame
        df = pd.read_csv(caminho_arquivo)
        # Obtém o tipo de arritmia (Type) e conta a quantidade de cada tipo
        tipo_arr = df['Type'].value_counts().to_dict()
        # Adiciona o tipo de arritmia e a quantidade à lista de dados
        dados.append(tipo_arr)

# Cria um DataFrame Pandas com os dados
df_resumo = pd.DataFrame(dados).fillna(0).astype(int)

# Soma as contagens de cada tipo de arritmia em todos os arquivos
resumo_final = df_resumo.sum().reset_index()
resumo_final.columns = ['Type', 'Quantidade']

# Caminho para o arquivo de resumo
caminho_resumo = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Summary.csv'

# Salva o resumo em um arquivo CSV
resumo_final.to_csv(caminho_resumo, index=False)
