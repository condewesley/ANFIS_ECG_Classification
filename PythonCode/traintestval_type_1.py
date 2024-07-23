import pandas as pd

# Caminho do arquivo Dataframe_Type_1.csv
file_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Dataframe_Type_1.csv'

# Caminhos para os arquivos de saída
output_train_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Train_Type_1.csv'
output_test_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Test_Type_1.csv'
output_validation_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\Validation_Type_1.csv'

# Ler os dados diretamente do arquivo CSV
with open(file_path, 'r') as file:
    lines = file.readlines()

# Dividir os dados em conjuntos de treinamento, teste e validação
train_data = ''.join(lines[:395])
test_data = ''.join(lines[396:479])
validation_data = ''.join(lines[480:563])

# Escrever os dados nos arquivos de saída
with open(output_train_path, 'w') as file:
    file.write(train_data)

with open(output_test_path, 'w') as file:
    file.write(test_data)

with open(output_validation_path, 'w') as file:
    file.write(validation_data)
