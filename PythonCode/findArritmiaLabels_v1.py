import pandas as pd
import os
from shutil import copyfile

# Paths dos arquivos
signals_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Filter'
annotations_path = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Annotations'
path_type_1 = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_1'
path_type_2 = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_2'
path_type_3 = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_3'
path_type_4 = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_4'
path_type_5 = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\Type_5'
path_high_labels = r'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\HighLabels'

# Dicionário para mapear tipos para números
tipos_para_numeros = {
    'A': 1,  # A (Atrial premature beat)
    'R': 2,  # R (Right bundle branch block beat)
    'L': 3,  # L (Left bundle branch block beat)
    '/': 4   # / (Paced beat)
}


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


# Leitura dos arquivos no diretório de sinais
for arquivo_sinal in os.listdir(signals_path):
    if arquivo_sinal.endswith(".csv"):
        range_ = obter_range(os.path.join(signals_path, arquivo_sinal))

        # Verificar se o intervalo MLII é válido
        if range_[1] - range_[0] < 0:
            print(f"Ignorando o arquivo {arquivo_sinal} devido ao intervalo MLII negativo.")
            continue

        # Leitura do sinal
        signals_filepath = os.path.join(signals_path, arquivo_sinal)
        # Leitura das amostras e seus tipos dentro do range do arquivo de anotação correspondente
        arquivo_anotacao = f"{arquivo_sinal.split('_')[0]}_atr.csv"
        amostras_tipos = obter_amostras_e_tipos(os.path.join(annotations_path, arquivo_anotacao), range_)

        # Verificar se todos os tipos dentro do range são iguais e correspondem a um dos tipos especificados,
        # ou se pelo menos um tipo especificado está presente junto com o tipo 'N'
        tipos_presentes = set(amostras_tipos['Type'])
        tipos_validos = tipos_presentes.intersection(tipos_para_numeros.keys())
        if len(tipos_presentes - tipos_para_numeros.keys()) == 0 and (
                ('N' in tipos_presentes and tipos_validos) or len(tipos_presentes) == 1):
            # Copiar o arquivo para o diretório correspondente ao tipo
            tipo_valido = tipos_presentes.pop() if len(tipos_presentes) == 1 else tipos_validos.pop()
            destino = os.path.join(globals()[f'path_type_{tipos_para_numeros[tipo_valido]}'],
                                   arquivo_sinal.replace('.csv', f'_Type_{tipos_para_numeros[tipo_valido]}.csv'))
            copyfile(signals_filepath, destino)
            print(f"Arquivo {arquivo_sinal} copiado com sucesso para {destino}")
        else:
            # Se não atender aos critérios, copiar o arquivo para o diretório 'HighLabels'
            destino = os.path.join(path_high_labels, arquivo_sinal)
            copyfile(signals_filepath, destino)
            print(f"Arquivo {arquivo_sinal} copiado com sucesso para {destino}")
