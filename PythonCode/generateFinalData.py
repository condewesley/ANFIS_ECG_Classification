import os

# Caminho dos arquivos de entrada e saída
input_dir = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database'
output_dir = os.path.join(input_dir, 'Dataframe')

# Criar o diretório de saída se ele não existir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Função para combinar os dados dos arquivos de tipo 0 e 1
def combine_files(input_file_0, input_file_1, output_file):
    with open(input_file_0, 'r', encoding='utf-8') as file0, \
            open(input_file_1, 'r', encoding='utf-8') as file1, \
            open(output_file, 'w', encoding='utf-8') as output:

        # Copiar os dados do arquivo de tipo 0 para o arquivo de saída
        for line in file0:
            output.write(line)

        # Pular uma linha antes de inserir os dados do arquivo de tipo 1
        output.write('\n')

        # Copiar os dados do arquivo de tipo 1 para o arquivo de saída
        for line in file1:
            output.write(line)


# Combine para Train.csv
combine_files(os.path.join(input_dir, 'Train_Type_0.csv'), os.path.join(input_dir, 'Train_Type_1.csv'),
              os.path.join(output_dir, 'Train.csv'))

# Combine para Test.csv
combine_files(os.path.join(input_dir, 'Test_Type_0.csv'), os.path.join(input_dir, 'Test_Type_1.csv'),
              os.path.join(output_dir, 'Test.csv'))

# Combine para Validation.csv
combine_files(os.path.join(input_dir, 'Validation_Type_0.csv'), os.path.join(input_dir, 'Validation_Type_1.csv'),
              os.path.join(output_dir, 'Validation.csv'))
