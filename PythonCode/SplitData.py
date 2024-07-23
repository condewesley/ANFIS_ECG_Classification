import os
import random
import shutil

# Diretórios de origem e destino
source_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\FinalDataset'
destination_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\FinalDataset\SplitData'

# Tipos de arquivos
types = [1, 2, 3, 4, 5]

# Porcentagens de divisão
train_percentage = 0.7
test_percentage = 0.15
validation_percentage = 0.15

# Para cada tipo
for tipo in types:
    # Pasta de origem e destino para o tipo atual
    source_folder = os.path.join(source_dir, f'Type_{tipo}')
    train_folder = os.path.join(destination_dir, f'Type_{tipo}_Train')
    test_folder = os.path.join(destination_dir, f'Type_{tipo}_Test')
    validation_folder = os.path.join(destination_dir, f'Type_{tipo}_Validation')

    # Verificar se as pastas de destino existem e, se não, criá-las
    for folder in [train_folder, test_folder, validation_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Lista de arquivos nesta pasta
    files = os.listdir(source_folder)

    # Embaralhar a lista de arquivos
    random.shuffle(files)

    # Calcular quantidades para cada conjunto
    total_files = len(files)
    train_count = int(total_files * train_percentage)
    test_count = int(total_files * test_percentage)

    # Copiar arquivos para a pasta de treinamento
    for file in files[:train_count]:
        source_file = os.path.join(source_folder, file)
        destination_file = os.path.join(train_folder, file)
        shutil.copyfile(source_file, destination_file)

    # Copiar arquivos para a pasta de teste
    for file in files[train_count:train_count + test_count]:
        source_file = os.path.join(source_folder, file)
        destination_file = os.path.join(test_folder, file)
        shutil.copyfile(source_file, destination_file)

    # Copiar o restante dos arquivos para a pasta de validação
    for file in files[train_count + test_count:]:
        source_file = os.path.join(source_folder, file)
        destination_file = os.path.join(validation_folder, file)
        shutil.copyfile(source_file, destination_file)

print("Concluído! Os arquivos foram divididos e copiados para os diretórios de treinamento, teste e validação.")
