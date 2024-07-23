import pandas as pd

# Define o diretório e o nome do arquivo
directory = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database'
file_name = 'Dataframe_Type_0.csv'

# Carrega o arquivo CSV em um DataFrame
df = pd.read_csv(f'{directory}\\{file_name}')

# Define os índices para divisão dos dados
indices_train = (1, 405)
indices_test = (405, 492)
indices_validation = (492, 579)

# Divide os dados em conjuntos de treino, teste e validação
train_data = df.iloc[indices_train[0]-1:indices_train[1]-1]
test_data = df.iloc[indices_test[0]-1:indices_test[1]-1]
validation_data = df.iloc[indices_validation[0]-1:indices_validation[1]-1]

# Define os nomes dos arquivos de saída
train_file_name = 'Train_Type_0.csv'
test_file_name = 'Test_Type_0.csv'
validation_file_name = 'Validation_Type_0.csv'

# Salva os dados divididos em arquivos CSV
train_data.to_csv(f'{directory}\\{train_file_name}', index=False)
test_data.to_csv(f'{directory}\\{test_file_name}', index=False)
validation_data.to_csv(f'{directory}\\{validation_file_name}', index=False)

file_name = 'Dataframe_Type_0.csv'

# Carrega o arquivo CSV em um DataFrame
df = pd.read_csv(f'{directory}\\{file_name}')

# Define os índices para divisão dos dados
indices_train = (1, 405)
indices_test = (405, 492)
indices_validation = (492, 579)

# Divide os dados em conjuntos de treino, teste e validação
train_data = df.iloc[indices_train[0]-1:indices_train[1]-1]
test_data = df.iloc[indices_test[0]-1:indices_test[1]-1]
validation_data = df.iloc[indices_validation[0]-1:indices_validation[1]-1]

# Define os nomes dos arquivos de saída
train_file_name = 'Train_Type_0.csv'
test_file_name = 'Test_Type_0.csv'
validation_file_name = 'Validation_Type_0.csv'

# Salva os dados divididos em arquivos CSV
train_data.to_csv(f'{directory}\\{train_file_name}', index=False)
test_data.to_csv(f'{directory}\\{test_file_name}', index=False)
validation_data.to_csv(f'{directory}\\{validation_file_name}', index=False)