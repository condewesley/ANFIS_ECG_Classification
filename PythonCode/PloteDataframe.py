import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo CSV
file_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Dataframe\Train.csv'
linha = 700

# Carregar o arquivo CSV
df = pd.read_csv(file_path, header=None)

# Extrair os valores da linha especificada (considerando que o tipo está na coluna 21601)
values = df.iloc[linha, 0:21599].values  # Extraindo os valores da coluna 1 até 21600

# Verificar o tipo na última coluna
tipo = df.iloc[linha, 21600]  # considerando que o tipo está na coluna 21601

# Definir o título com base no tipo
titulo = 'Normal' if tipo == 0 else 'Arritmia'

# Plotar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(values) + 1), values, linewidth=0.5, label=f'Linha {linha}')
plt.title(f'Gráfico da Linha {linha} - MLII ({titulo})')
plt.xlabel('Sample')
plt.ylabel('MLII')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
