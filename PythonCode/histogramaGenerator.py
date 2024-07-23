import os
import pandas as pd
import matplotlib.pyplot as plt

# Caminho para as anotações
annotations_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Annotations'

# Caminho para os sinais divididos
signals_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Signals_Split'

# Dicionário para mapear os tipos de anotação para suas descrições em português brasileiro
type_descriptions = {
    'A': 'Batimento prematuro atrial',
    'a': 'Batimento prematuro atrial aberrante',
    'J': 'Batimento prematuro nodal (juncional)',
    'S': 'Batimento prematuro supraventricular',
    'V': 'Contração ventricular prematura',
    'E': 'Batimento de escape ventricular',
    'L': 'Batimento com bloqueio de ramo esquerdo',
    'R': 'Batimento com bloqueio de ramo direito',
    'F': 'Fusão de batimento ventricular e normal',
    'e': 'Batimento de escape atrial',
    'j': 'Batimento de escape nodal (juncional)',
    '/': 'Batimento artificial',
    'f': 'Fusão de batimento artificial e normal'
}

# Tipos de anotações a serem procurados
types_to_search = list(type_descriptions.keys())

# Dicionário para contar os tipos encontrados
type_counts = {type: 0 for type in types_to_search}

# Iterar sobre os arquivos de anotação
for annotation_file in os.listdir(annotations_path):
    if annotation_file.endswith('_atr.csv'):
        # Extrair o ID do arquivo de anotação
        id = annotation_file.split('_')[0]

        # Ler o arquivo de anotação
        df_annotation = pd.read_csv(os.path.join(annotations_path, annotation_file))

        # Iterar sobre as linhas do arquivo de anotação
        for index, row in df_annotation.iterrows():
            annotation_type = row['Type']
            if annotation_type in types_to_search:
                type_counts[annotation_type] += 1

                # Encontrar o arquivo de sinal correspondente
                signal_file = f'{id}_ecg_1.csv'
                if os.path.exists(os.path.join(signals_path, signal_file)):
                    # Aqui você pode fazer algo com o arquivo de sinal, se necessário
                    pass

# Calcular a quantidade total
total_count = sum(type_counts.values())

# Gerar o histograma
plt.figure(figsize=(10, 6))
plt.bar([type_descriptions[type] for type in type_counts.keys()], type_counts.values(), color='gray')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Tipo de Anotação')
plt.ylabel('Quantidade')
plt.title('Histograma de Tipos de Anotação')
plt.grid(True, linestyle='--', alpha=0.7)
for i, v in enumerate(type_counts.values()):
    plt.text(i, v + 1, f'{v}', ha='center', fontweight='bold')
plt.text(len(type_counts) - 1, -total_count * 0.15, f'Total: {total_count}', ha='right', fontweight='bold')
plt.tight_layout()
plt.show()
