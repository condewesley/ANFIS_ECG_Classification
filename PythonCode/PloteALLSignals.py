import os
import pandas as pd
import matplotlib.pyplot as plt
import time

# Caminho para os arquivos .csv
path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_1'

# Listar todos os arquivos .csv no diretório
csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]

# Variável para indicar se começar a plotar
comecar_plotar = False

# Plotar os arquivos .csv separadamente
for csv_file in csv_files:
    if csv_file == '232_ecg_577_Type_1.csv':
        comecar_plotar = True

    if comecar_plotar:
        # Ler o arquivo .csv
        df = pd.read_csv(os.path.join(path, csv_file))

        # Extrair os dados
        samples = df['Sample']
        mlii = df['MLII']

        # Plotar
        plt.plot(samples, mlii)
        plt.xlabel('Sample')
        plt.ylabel('MLII')
        plt.title(f'Arquivo: {csv_file}')
        plt.show()

        # Esperar 2 segundos antes de ir para o próximo arquivo
        time.sleep(0.5)
