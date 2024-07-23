% Defina o caminho para os arquivos .csv
caminho = 'C:\Users\Wesley\Desktop\TCC_Project\MIT-BIH_Arrhythmia_Database\OficialDataset\FinalDataset\SplitData';

% Nomes dos arquivos
arquivos = {'Train.csv', 'Validation.csv', 'Test.csv'};

% Loop através dos arquivos
for i = 1:length(arquivos)
    % Carregar arquivo .csv
    arquivo_csv = fullfile(caminho, arquivos{i});
    dados_csv = readmatrix(arquivo_csv); % Assumindo que os dados são todos numéricos
    
    % Salvar como .mat
    [~, nome_arquivo, ~] = fileparts(arquivo_csv);
    arquivo_mat = fullfile(caminho, [nome_arquivo '.mat']);
    save(arquivo_mat, 'dados_csv');
    
    % Carregar no workspace
    variavel_nome = genvarname(nome_arquivo); % Nome da variável no workspace
    load(arquivo_mat, variavel_nome);
    assignin('base', variavel_nome, dados_csv);
end

% Limpar variáveis temporárias
clear arquivo_csv dados_csv nome_arquivo arquivo_mat variavel_nome caminho arquivos i;
