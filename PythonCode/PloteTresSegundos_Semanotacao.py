import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo CSV
file_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_0\100_ecg_3_Type_0.csv'

# Leitura do arquivo CSV
df = pd.read_csv(file_path)

# Extração dos dados de Sample e MLII
sample = df['Sample']
ml_ii = df['MLII']

# Plot do sinal ECG
plt.figure(figsize=(12, 6))
plt.plot(sample, ml_ii, color='red', label='MLII', linewidth=0.5)
plt.title('Sinal ECG - 100_ecg_3_Type_0.csv')
plt.xlabel('Amostras')
plt.ylabel('Amplitude (mV)')
plt.grid(True)
plt.legend()

plt.show()
