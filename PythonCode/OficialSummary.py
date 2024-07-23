import pandas as pd
import os
import csv

# Path do diretório de anotações
annotations_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Annotations'
# Path para salvar o arquivo de resumo
summary_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Summary.csv'

# Tipos a verificar
tipos_a_verificar = {'N': 0, 'A': 1, 'R': 2, 'L': 3, '/': 4}

# Função para contar as ocorrências de cada tipo de anotação
def contar_ocorrencias(arquivo):
    df_annotations = pd.read_csv(arquivo, names=['Sample', 'Type'])
    ocorrencias = df_annotations['Type'].value_counts().reindex(tipos_a_verificar.keys()).fillna(0).astype(int)
    sinal_id = os.path.splitext(os.path.basename(arquivo))[0].split('_')[0]
    return sinal_id, ocorrencias

# Lista de todos os arquivos de anotações no diretório
arquivos_anotacoes = [os.path.join(annotations_path, arquivo) for arquivo in os.listdir(annotations_path) if arquivo.endswith('_atr.csv')]

# Lista para armazenar os resultados de cada arquivo
resumos = []

# Gerar resumo para cada arquivo
for arquivo in arquivos_anotacoes:
    sinal_id, ocorrencias = contar_ocorrencias(arquivo)
    resumo = {'Sinal': sinal_id}
    resumo.update(ocorrencias)
    resumos.append(resumo)

# Salvar os resumos em um arquivo CSV
with open(summary_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Sinal', 'N', 'A', 'R', 'L', '/'])
    writer.writeheader()
    writer.writerows(resumos)

print("Resumos salvos com sucesso em:", summary_path)
