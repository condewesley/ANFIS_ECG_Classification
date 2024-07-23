import pandas as pd
import os

# Diretório de origem
source_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\FinalDataset'

# Tipos de arquivos
types = [0, 1, 2, 3, 4]

# Para cada tipo
for tipo in types:
    # Pasta correspondente ao tipo
    folder = os.path.join(source_dir, f'Type_{tipo}')

    # Lista de arquivos nesta pasta
    files = os.listdir(folder)

    # Para cada arquivo
    for file in files:
        # Verificar se é um arquivo CSV
        if file.endswith('.csv'):
            # Caminho completo do arquivo
            csv_file_path = os.path.join(folder, file)

            # Ler o arquivo CSV
            df = pd.read_csv(csv_file_path)

            # Obter o último Sample
            last_sample = df['Sample'].iloc[-1]

            # Adicionar a nova linha com o Sample e o valor do tipo
            new_row = {'Sample': last_sample + 1, 'MLII': tipo}
            df = df._append(new_row, ignore_index=True)

            # Salvar o arquivo CSV de volta
            output_file_path = os.path.join(folder, file)
            df.to_csv(output_file_path, index=False)

print("Concluído! As modificações foram aplicadas a todos os arquivos CSV.")
