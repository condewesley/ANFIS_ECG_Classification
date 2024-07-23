import os
import shutil
import pandas as pd

# Diretório de origem
source_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset'

# Diretório de destino
destination_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\FinalDataset'

# Lista dos tipos de pastas
type_folders = ['Type_0', 'Type_1', 'Type_2', 'Type_3', 'Type_4']

# Quantidade de arquivos a serem copiados de cada tipo
files_to_copy = 246

# Para cada tipo de pasta
for folder in type_folders:
    source_folder = os.path.join(source_dir, folder)
    destination_folder = os.path.join(destination_dir, folder)

    # Criar pasta de destino se não existir
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Lista de arquivos no tipo de pasta
    files = os.listdir(source_folder)
    # Selecionar os primeiros 'files_to_copy' arquivos
    files = files[:files_to_copy]

    copied_files = 0  # Contador de arquivos copiados
    # Copiar cada arquivo para o destino
    for file in files:
        source_file = os.path.join(source_folder, file)
        destination_file = os.path.join(destination_folder, file)

        # Carregar o arquivo CSV
        df = pd.read_csv(source_file)

        # Adicionar uma linha extra com Sample e MLII
        last_sample = int(df.iloc[-1]['Sample'])  # Converter para inteiro para remover o ".0"
        new_sample = last_sample + 1
        new_row = {'Sample': new_sample, 'MLII': folder[-1]}
        df = df._append(new_row, ignore_index=True)

        # Salvar o DataFrame atualizado
        df.to_csv(destination_file, index=False)

        copied_files += 1

        # Se já copiamos o número necessário de arquivos, pare o loop
        if copied_files == files_to_copy:
            break

print("Concluído! Os arquivos foram copiados para o diretório final.")
