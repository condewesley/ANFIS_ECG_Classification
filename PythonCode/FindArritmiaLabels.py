import os
import pandas as pd
import shutil

# Definição dos tipos
types = {
    'A': 1,  # A (Atrial premature beat)
    'V': 2,  # V (Premature ventricular contraction)
    'R': 3,  # R (Right bundle branch block beat)
    'L': 4,  # L (Left bundle branch block beat)
    '/': 5   # / (Paced beat)
}

# Caminho para os diretórios de anotações e sinais
annotations_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Annotations'
signals_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Signals_Split'
output_base_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset'

# Função para verificar se o sinal é válido
def check_valid_signal(types_list):
    num_N = types_list.count('N')
    if num_N == 1 or num_N == 2:
        for type_key in types.keys():
            if type_key in types_list:
                return True
    return False

# Iterar sobre todos os arquivos de anotações
for filename in os.listdir(annotations_dir):
    if filename.endswith('_atr.csv'):
        # Obter o ID do sinal a partir do nome do arquivo
        signal_id = filename.split('_')[0]

        # Ler o arquivo de anotações
        annotations_df = pd.read_csv(os.path.join(annotations_dir, filename))

        # Verificar se há 2 valores de N seguidos e algum dos tipos especificados
        types_list = annotations_df['Type'].tolist()
        if check_valid_signal(types_list):
            print(f"Sinais encontrados com 1 ou 2 tipos N e algum dos Types determinados no arquivo {filename}:")
            print("Sample | MLII | Type")

            # Iterar sobre todos os arquivos de sinais
            for signal_file in os.listdir(signals_dir):
                if signal_file.startswith(f"{signal_id}_ecg_"):
                    signal_path = os.path.join(signals_dir, signal_file)
                    signals_df = pd.read_csv(signal_path)
                    # Verificar se a coluna MLII está presente no arquivo de sinais
                    if 'MLII' not in signals_df.columns:
                        print(f"Aviso: O arquivo de sinais {signal_file} não contém a coluna MLII. Ignorando.")
                        continue

                    # Verificar se o sinal é válido
                    if check_valid_signal(types_list):
                        # Encontrar o tipo presente no sinal
                        signal_type = next((type_key for type_key in types.keys() if type_key in types_list), None)
                        if signal_type:
                            type_value = types[signal_type]
                            annotations_type_df = annotations_df[annotations_df['Type'] == signal_type]

                            # Copiar o arquivo de sinal correspondente e renomeá-lo
                            output_dir = os.path.join(output_base_dir, f"Type_{type_value}")
                            if not os.path.exists(output_dir):
                                os.makedirs(output_dir)
                            shutil.copyfile(signal_path, os.path.join(output_dir, f"{signal_file.split('.')[0]}_Type_{type_value}.csv"))

                            # Mostrar valores encontrados
                            for index, row in annotations_type_df.iterrows():
                                sample = row['Sample']
                                ml_ii_value = signals_df.loc[signals_df['Sample'] == sample, 'MLII'].values
                                if len(ml_ii_value) > 0:
                                    print(f"{sample} | {ml_ii_value[0]} | {row['Type']}")
                                    if sample > 720:
                                        break
        else:
            print(f"Nenhum sinal encontrado com 1 ou 2 tipos N e algum dos Types determinados no arquivo {filename}")
