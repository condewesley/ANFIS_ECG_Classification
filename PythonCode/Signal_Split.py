import pandas as pd
import os
import glob

# Definir o caminho para o diretório de entrada e o diretório de saída
input_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Signals'
output_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Signals_Split'

# Verificar se o diretório de saída existe, se não, criar
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Listar todos os arquivos .csv no diretório de entrada
csv_files = glob.glob(os.path.join(input_path, '*.csv'))

for file_path in csv_files:
    try:
        # Carregar o arquivo CSV original
        data = pd.read_csv(file_path)
        if 'MLII' not in data.columns or 'Sample' not in data.columns:
            print(f'O arquivo {os.path.basename(file_path)} não contém a coluna MLII ou Sample. Indo para o próximo arquivo.')
            continue
    except Exception as e:
        print(f"Erro ao processar o arquivo {os.path.basename(file_path)}: {e}")
        continue

    # Definir o número de amostras por arquivo
    samples_per_file = 1080  # Alteração para 1080 amostras (3 segundos)
    total_samples = len(data)
    num_files = total_samples // samples_per_file

    # Dividir os dados em partes e salvar em arquivos separados
    for i in range(num_files):
        start_idx = i * samples_per_file
        end_idx = start_idx + samples_per_file - 1
        subset_data = data.loc[start_idx:end_idx, ['Sample', 'MLII']]  # Selecionar as colunas Sample e MLII

        # Salvar o subset em um novo arquivo CSV
        file_name = os.path.basename(file_path)
        file_name_without_extension = os.path.splitext(file_name)[0]
        output_filename = f'{file_name_without_extension}_{i + 1}.csv'
        output_file_path = os.path.join(output_path, output_filename)
        subset_data.to_csv(output_file_path, index=False)

    print(f'Arquivos divididos para {file_name_without_extension} gerados com sucesso.')

print('Todos os arquivos foram processados.')
