import os
import pandas as pd

# Caminho para o diretório
path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\FinalDataset\Type_4'

# Listar todos os arquivos .csv no diretório
csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]

# Renomear os arquivos .csv alterando o último número para 2
for csv_file in csv_files:
    # Separar o nome do arquivo e a extensão
    filename, file_extension = os.path.splitext(csv_file)

    # Verificar se o último caractere do nome do arquivo é um número
    if filename[-1].isdigit():
        # Construir o novo nome do arquivo com o último número alterado para 2
        new_filename = filename[:-1] + '5' + file_extension

        # Renomear o arquivo
        os.rename(os.path.join(path, csv_file), os.path.join(path, new_filename))

        # Abrir o arquivo CSV e alterar o último valor da coluna MLII
        csv_path = os.path.join(path, new_filename)
        df = pd.read_csv(csv_path)

        # Obter o valor alterado do último caractere do nome do arquivo
        new_last_digit = int(new_filename[-5])  # Pega o último dígito antes da extensão '.csv'

        # Alterar o último valor da coluna MLII
        df.loc[df.index[-1], 'MLII'] = new_last_digit

        # Salvar as alterações no arquivo CSV
        df.to_csv(csv_path, index=False)

        print(f"Arquivo renomeado e valor alterado: {csv_file} -> {new_filename}")
    else:
        print(f"Não foi possível renomear o arquivo {csv_file}: Último caractere não é um número.")
