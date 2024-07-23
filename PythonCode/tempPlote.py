import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo CSV
file_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_2\205_ecg_153_Type_2.csv'

# Leitura do arquivo CSV
df = pd.read_csv(file_path)

# Extração dos dados de Sample e MLII
sample = df['Sample']
mlii = df['MLII']

# Plot do gráfico no formato de um ECG
plt.figure(figsize=(10, 6))
plt.plot(sample, mlii, color='blue')
plt.title('ECG - 205_ecg_153_Type_2')
plt.xlabel('Tempo (ms)')
plt.ylabel('Amplitude (mV)')
plt.grid(True)
plt.show()
