import pandas as pd
import os
from tabulate import tabulate

# Path dos arquivos
signals_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Signals_Split'
annotations_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Annotations'

# Função para ler o arquivo CSV e retornar o range de amostras
def obter_range(filepath):
    df = pd.read_csv(filepath)
    primeiro_valor = df['Sample'].iloc[0]
    ultimo_valor = df['Sample'].iloc[-1]
    return primeiro_valor, ultimo_valor

# Função para obter amostras e seus tipos dentro de um determinado range
def obter_amostras_e_tipos(filepath, range_):
    df = pd.read_csv(filepath)
    amostras_tipo = df[(df['Sample'] >= range_[0]) & (df['Sample'] <= range_[1])]
    return amostras_tipo[['Sample', 'Type']]

# Função para ler os valores de MLII para as amostras fornecidas
def ler_valores_MLII(filepath, amostras):
    df = pd.read_csv(filepath)
    valores_MLII = df[df['Sample'].isin(amostras)]
    return valores_MLII[['Sample', 'MLII']]

# Leitura do range de amostras do arquivo 100_ecg_1.csv
signals_filepath = os.path.join(signals_path, '100_ecg_3.csv')
range_ = obter_range(signals_filepath)

# Leitura das amostras e seus tipos dentro do range do arquivo 100_atr.csv
annotations_filepath = os.path.join(annotations_path, '100_atr.csv')
amostras_tipos = obter_amostras_e_tipos(annotations_filepath, range_)

# Leitura dos valores de MLII para as amostras obtidas
valores_MLII = ler_valores_MLII(signals_filepath, amostras_tipos['Sample'])

# Criar uma tabela para imprimir os resultados
tabela = pd.merge(valores_MLII, amostras_tipos, on='Sample')
print(tabulate(tabela, headers='keys', tablefmt='grid', showindex=False))
