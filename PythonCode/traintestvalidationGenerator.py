import os

# Diretório de origem e destino
source_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\FinalDataset\SplitData'
destination_dir = source_dir  # Pasta de destino é a mesma do origem

# Tipos de arquivos
types = [1, 2, 3, 4, 5]

# Finalidades
finalidades = ['Train', 'Test', 'Validation']

# Para cada finalidade
for finalidade in finalidades:
    # Caminho para o arquivo principal que será gerado
    output_file_path = os.path.join(destination_dir, f'{finalidade}.csv')

    # Abre o arquivo principal no modo de escrita
    with open(output_file_path, 'w') as f:
        # Para cada tipo
        for tipo in types:
            # Caminho para a pasta específica de tipo e finalidade
            folder_path = os.path.join(source_dir, f'Type_{tipo}_{finalidade}')

            # Lista de arquivos CSV nesta pasta
            files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

            # Ordena os arquivos pelo nome
            files.sort()

            # Para cada arquivo CSV nesta pasta
            for file in files:
                # Caminho completo do arquivo CSV
                file_path = os.path.join(folder_path, file)

                # Ler o arquivo CSV e adicionar os dados de MLII como uma linha
                with open(file_path, 'r') as csv_file:
                    next(csv_file)  # Pula o cabeçalho
                    ml_ii_data = [line.strip().split(',')[1] for line in csv_file]  # Lê os dados de MLII

                    # Escreve os dados de MLII no arquivo principal
                    f.write(','.join(
                        ml_ii_data) + '\n')  # Adiciona uma linha em branco entre os dados de diferentes arquivos

print("Concluído! Arquivos principais foram criados com sucesso.")
