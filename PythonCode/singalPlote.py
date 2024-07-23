import pandas as pd
import os
import matplotlib.pyplot as plt

type_id = 0
id_number = 100
number_count = 3

# Path dos arquivos
signals_path = fr'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_{type_id}'
#signals_path = fr'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Filter'
#signals_path = fr'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Signals_Split'
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
signals_filepath = os.path.join(signals_path, f'{id_number}_ecg_{number_count}_Type_{type_id}.csv')
#signals_filepath = os.path.join(signals_path, f'{id_number}_ecg_{number_count}.csv')
range_ = obter_range(signals_filepath)

# Leitura das amostras e seus tipos dentro do range do arquivo 100_atr.csv
annotations_filepath = os.path.join(annotations_path, f'{id_number}_atr.csv')
amostras_tipos = obter_amostras_e_tipos(annotations_filepath, range_)

# Leitura dos valores de MLII para as amostras obtidas
valores_MLII = ler_valores_MLII(signals_filepath, amostras_tipos['Sample'])

# Adicionando o segundo gráfico do ECG
# Caminho para o arquivo CSV
file_path = fr'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_{type_id}\{id_number}_ecg_{number_count}_Type_{type_id}.csv'
#file_path = fr'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Filter\{id_number}_ecg_{number_count}.csv'
#file_path = fr'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Signals_Split\{id_number}_ecg_{number_count}.csv'

# Leitura do arquivo CSV
df = pd.read_csv(file_path)

# Extração dos dados de Sample e MLII
sample = df['Sample']
mlii = df['MLII']

# Plot do gráfico no formato de um ECG
plt.figure(figsize=(10, 6))
plt.plot(sample, mlii, color='red', label='Sinal do ECG', linewidth=0.5)  # Linha mais fina
for _, row in amostras_tipos.iterrows():
    plt.plot(row['Sample'], valores_MLII[valores_MLII['Sample'] == row['Sample']]['MLII'].iloc[0], 'ko', markersize=3)  # Marcadores pretos e menores
    plt.text(row['Sample'], valores_MLII[valores_MLII['Sample'] == row['Sample']]['MLII'].iloc[0], row['Type'], ha='right', va='bottom', fontsize=12)
plt.title(f'ECG - {id_number}_ecg_{number_count}_Type_{type_id}')
plt.xlabel('Amostras')
plt.ylabel('Amplitude (mV)')
plt.grid(True)
plt.legend()

plt.show()
