import os
import pandas as pd

# Caminho para o diretório com os arquivos de sinais
diretorio_sinais = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Signals'

# Caminho para o diretório onde os arquivos serão salvos
diretorio_destino = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Temp_Signals'

# Lista todos os arquivos no diretório
arquivos_csv = [arquivo for arquivo in os.listdir(diretorio_sinais) if arquivo.endswith('.csv')]

# Loop sobre todos os arquivos .csv
for arquivo_csv in arquivos_csv:
    # Caminho completo para o arquivo .csv de entrada
    caminho_arquivo_entrada = os.path.join(diretorio_sinais, arquivo_csv)

    # Ler o arquivo CSV como DataFrame
    df_sinal = pd.read_csv(caminho_arquivo_entrada)

    # Inserir a coluna Sample no início do DataFrame
    df_sinal.insert(0, 'Sample', range(1, len(df_sinal) + 1))

    # Caminho completo para o arquivo .csv de saída
    caminho_arquivo_saida = os.path.join(diretorio_destino, arquivo_csv)

    # Salvar o DataFrame modificado como um novo arquivo CSV
    df_sinal.to_csv(caminho_arquivo_saida, index=False)

    print(f'Arquivo {arquivo_csv} processado e salvo com a coluna Sample.')
