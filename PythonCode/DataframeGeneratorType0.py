import os
import pandas as pd

# Caminho para a pasta com os arquivos de entrada
input_folder_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Type_0'

# Caminho para o arquivo de saída
output_file_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Dataframe_Type_0.csv'

# Inicializar uma lista para armazenar os dados MLII de todos os arquivos
ml2_data_list = []

# Iterar sobre todos os arquivos na pasta Type_0
for file_name in os.listdir(input_folder_path):
    if file_name.endswith('.csv'):
        # Caminho completo para o arquivo de entrada
        input_file_path = os.path.join(input_folder_path, file_name)

        # Carregar apenas os dados MLII do arquivo de entrada
        df = pd.read_csv(input_file_path, usecols=['MLII'])

        # Converter os dados da coluna MLII em uma única linha separada por vírgula e adicionar '0.0' no final
        ml2_data = ','.join(map(str, df['MLII'].values.tolist())) + ',0.0'

        # Adicionar os dados MLII à lista
        ml2_data_list.append(ml2_data)

# Salvar os dados MLII de todos os arquivos em linhas separadas no arquivo de saída
with open(output_file_path, 'w') as f:
    for ml2_data in ml2_data_list:
        f.write(ml2_data + '\n')

print("Arquivo salvo com sucesso em:", output_file_path)
