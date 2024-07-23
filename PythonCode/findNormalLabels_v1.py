import pandas as pd
import os
from shutil import copyfile

# Path dos arquivos
signals_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Signals_Split'
annotations_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Annotations'
path_type_0 = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_0'
path_filter = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Filter'
path_low_n = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\LowN'

# Tipos para verificar
tipos_a_verificar = {'A': 1, 'R': 2, 'L': 3, '/': 4}


# Função para ler o arquivo CSV e retornar o range de amostras
def obter_range(filepath):
    df = pd.read_csv(filepath)
    primeiro_valor = df['Sample'].iloc[0]
    ultimo_valor = df['Sample'].iloc[-1]
    return primeiro_valor, ultimo_valor


# Função para obter amostras e seus tipos dentro de um determinado range
def obter_amostras_e_tipos(filepath, range_):
    df = pd.read_csv(filepath)
    amostras_tipo = df[(df['Sample'] >= range_[0]) & (df['Sample'] <= range_[1])]
    return amostras_tipo[['Sample', 'Type']]


# Função para verificar se todas as amostras no range têm Type 'N'
def todas_amostras_sao_tipo_N(amostras_tipos):
    return all(amostras_tipos['Type'] == 'N')


# Função para verificar se há tipos específicos nas amostras
def verificar_tipos(amostras_tipos, tipos_a_verificar):
    for tipo in tipos_a_verificar:
        if tipo in amostras_tipos['Type'].values:
            return True
    return False


# Leitura dos arquivos no diretório de sinais
for arquivo_sinal in os.listdir(signals_path):
    if arquivo_sinal.endswith(".csv"):
        range_ = obter_range(os.path.join(signals_path, arquivo_sinal))
        # Leitura do sinal
        signals_filepath = os.path.join(signals_path, arquivo_sinal)
        # Leitura das amostras e seus tipos dentro do range do arquivo de anotação correspondente
        id_arquivo = arquivo_sinal.split('_')[0]
        arquivo_anotacao = f"{id_arquivo}_atr.csv"
        amostras_tipos = obter_amostras_e_tipos(os.path.join(annotations_path, arquivo_anotacao), range_)

        # Verificar se todas as amostras no range têm Type 'N'
        if todas_amostras_sao_tipo_N(amostras_tipos):
            # Se sim, copiar o arquivo para o diretório 'Type_0'
            destino = os.path.join(path_type_0, arquivo_sinal.replace('.csv', f'_Type_0.csv'))
            copyfile(signals_filepath, destino)
            print(f"Arquivo {arquivo_sinal} copiado com sucesso para {destino}")
        # Verificar se há tipos específicos dentro do range
        elif verificar_tipos(amostras_tipos, tipos_a_verificar):
            # Se houver, copiar o arquivo para o diretório 'Filter'
            destino = os.path.join(path_filter, arquivo_sinal)
            copyfile(signals_filepath, destino)
            print(f"Arquivo {arquivo_sinal} copiado com sucesso para {destino}")
        else:
            # Se não, copiar o arquivo para o diretório 'LowN'
            destino = os.path.join(path_low_n, arquivo_sinal)
            copyfile(signals_filepath, destino)
            print(f"Arquivo {arquivo_sinal} copiado com sucesso para {destino}")
