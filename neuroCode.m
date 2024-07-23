% Iniciar o cronômetro
tic;

% Fazendo cópias dos dados
Input_Train_All_Copy = Input_Train_All;
Input_Test_All_Copy = Input_Test_All;
Input_Validation_All_Copy = Input_Validation_All;

% Inputs
%       1            2         3          4           5        6        7
% [R_amplitude, min_signal, energy, mean_signal, std_signal, dp_rr, num_beats, 
%       8                 9                 10
% max_RR_interval, min_RR_interval, mean_RR_interval, signal_type];

input_anfis = [1, 5, 6, 8, 9];

% Passo 2: Organizar os dados
X_train = Input_Train_All_Copy(:,input_anfis); % Características de treinamento
Y_train = Input_Train_All_Copy(:,end); % Rótulos de treinamento
X_test = Input_Test_All_Copy(:,input_anfis); % Características de teste
Y_test = Input_Test_All_Copy(:,end); % Rótulos de teste
X_val = Input_Validation_All_Copy(:,input_anfis); % Características de validação
Y_val = Input_Validation_All_Copy(:,end); % Rótulos de validação

% Ajuste dos parâmetros do modelo
opt = genfisOptions('SubtractiveClustering', 'ClusterInfluenceRange', 0.7); % Aumentando o raio de influência

fis = genfis(X_train, Y_train, opt);
epochs = 800; % Aumentando o número de épocas

% Separando os dados de validação
chkData = [X_val Y_val];

% Definindo as opções de treinamento
options = anfisOptions('InitialFIS', fis, 'ValidationData', chkData, 'EpochNumber', epochs);

% Treinando o modelo ANFIS
[net, trainError, ~, ~, valError] = anfis([X_train Y_train], options);

% Pegando trainError e valError apenas da net1
[trainError_net, valError_net] = deal(trainError, valError);

% Passo 4: Avaliar o desempenho da rede
Y_pred = evalfis(X_test, net);
Y_pred = round(Y_pred); % Arredonda para 0 ou 1

% Mapear os valores de 1 a 5 para os rótulos das classes correspondentes
class_labels = {'Normal', 'Batimento atrial prematuro', 'Batimento de bloqueio de ramo direito', 'Batimento de bloqueio de ramo esquerdo', 'Batimento com Marca-Passo'};

% Modificando os rótulos para garantir que estejam no intervalo de 1 a 5
Y_test = mod(Y_test, 5) + 1;
Y_pred = mod(Y_pred, 5) + 1;

% Calcular a matriz de confusão
conf_matrix = confusionmat(Y_test, Y_pred);

% Plotar a matriz de confusão
figure;
heatmap(conf_matrix, 'Colormap', parula(5), 'ColorLimits', [1 5], 'ColorbarVisible', 'on', ...
    'XLabel', 'Predicted Labels', 'YLabel', 'True Labels', 'Title', 'Confusion Matrix');
set(gcf, 'Color', 'w'); % Define o fundo da figura como branco

% Calcular as métricas para cada classe
accuracy = zeros(1, size(conf_matrix, 1));
sensitivity = zeros(1, size(conf_matrix, 1));
specificity = zeros(1, size(conf_matrix, 1));

for i = 1:size(conf_matrix, 1)
    true_positives = conf_matrix(i, i);
    false_negatives = sum(conf_matrix(i, :)) - true_positives;
    false_positives = sum(conf_matrix(:, i)) - true_positives;
    true_negatives = sum(conf_matrix(:)) - true_positives - false_negatives - false_positives;

    accuracy(i) = (true_positives + true_negatives) / sum(conf_matrix(:));
    sensitivity(i) = true_positives / (true_positives + false_negatives);
    specificity(i) = true_negatives / (true_negatives + false_positives);
end

% Print das métricas para cada classe
for i = 1:length(class_labels)
    disp(['Classe: ', class_labels{i}]);
    disp(['Acurácia: ', num2str(accuracy(i))]);
    disp(['Sensibilidade: ', num2str(sensitivity(i))]);
    disp(['Especificidade: ', num2str(specificity(i))]);
end

% Plotar o gráfico de superfície
% Rótulos correspondentes às entradas
input_labels = {'Amplitude R (mV)', 'Valor Mínimo', 'Energia', 'Média', 'Desvio Padrão (s)', ...
                'Desvio Padrão do Intervalo RR (s)', 'Número de Batimentos', 'Maior Intervalo RR (s)', 'Menor Intervalo RR (s)', 'Média dos Intervalos RR'};

% Escolha das entradas do FIS
chosen_inputs = 1:5; % Todos os valores de 1 a 5

% Escolher apenas as posições 4 e 5 de chosen_inputs para o gensurf
chosen_inputs_gensurf = chosen_inputs(4:5);

% Encontrar os rótulos das entradas selecionadas para o gensurf
selected_labels_gensurf = cell(1, numel(chosen_inputs_gensurf));
for i = 1:numel(chosen_inputs_gensurf)
    % Verificar se o índice escolhido está dentro do intervalo
    if chosen_inputs_gensurf(i) >= 1 && chosen_inputs_gensurf(i) <= numel(input_anfis)
        % Encontrar o rótulo da entrada selecionada
        selected_labels_gensurf{i} = input_labels{input_anfis(chosen_inputs_gensurf(i))};
    else
        error('Índice de entrada fora do intervalo.');
    end
end

% Plotar o gráfico de superfície com as entradas escolhidas
figure;
gensurf(fis, chosen_inputs_gensurf);
xlabel(selected_labels_gensurf{1});
ylabel(selected_labels_gensurf{2});
zlabel('Saída');
title('Superfície do Sistema de Inferência Fuzzy para Classificação de Arritmias');

% Plotar as funções de pertinência para todas as variáveis de entrada
num_plots = numel(chosen_inputs);
figure;
for i = 1:num_plots
    subplot(num_plots, 1, i); % Dividir a figura em subplots
    [x, mf] = plotmf(fis, 'input', chosen_inputs(i));
    plot(x, mf);
    title(['Função de pertinência da entrada ', num2str(chosen_inputs(i))]);
    xlabel(input_labels{input_anfis(chosen_inputs(i))});
    ylabel('Grau de Pertinência'); % Adicionando o rótulo do eixo Y
    legend(arrayfun(@(x) ['Função de Pertinência ' num2str(x)], 1:size(mf, 1), 'UniformOutput', false)); % Adicionando legendas para cada linha
end

% Plotar o erro de treinamento e validação
figure;
plot(trainError_net, '--', 'Color', [0.2, 0.6, 1], 'LineWidth', 1); % Linha pontilhada para o erro de treinamento
hold on;
plot(valError_net, '-', 'Color', [1, 0.6, 0.2], 'LineWidth', 1); % Linha contínua para o erro de validação
hold off;
legend('Erro de Treinamento', 'Erro de Validação', 'Location', 'Best');
xlabel('Épocas');
ylabel('Erro Quadrático Médio (RMSE)');
title('Curvas de Erro de Treinamento e Validação');
grid on; % Adicionar grades ao gráfico

% Adicionar o valor do RMSE ao gráfico
rmse_text = ['\bf{RMSE}: ', num2str(trainError_net(end))];
text(length(trainError_net), trainError_net(end) + 0.01*max(trainError_net), rmse_text, 'HorizontalAlignment', 'right', 'Color', 'k');

% Adicionar legenda
legend('show', 'Location', 'Best');

% Calcular as métricas gerais
overall_accuracy = sum(accuracy) / length(accuracy);
overall_sensitivity = sum(sensitivity) / length(sensitivity);
overall_specificity = sum(specificity) / length(specificity);

% Calcular a acurácia durante o treinamento e validação
trainAccuracy = 1 - trainError_net;
valAccuracy = 1 - valError_net;

% Plotar o gráfico de acurácia
figure;
plot(trainAccuracy, '--', 'Color', [0.2, 0.6, 1], 'LineWidth', 1); % Linha pontilhada para a acurácia de treinamento
hold on;
plot(valAccuracy, '-', 'Color', [1, 0.6, 0.2], 'LineWidth', 1); % Linha contínua para a acurácia de validação
hold off;
legend('Acurácia de Treinamento', 'Acurácia de Validação', 'Location', 'Best');
xlabel('Épocas');
ylabel('Acurácia');
title('Curvas de Acurácia de Treinamento e Validação');
grid on; % Adicionar grades ao gráfico

% Adicionar o valor do RMSE ao gráfico
acuracia_text = ['\bf{Acurácia}: ', num2str(trainAccuracy(end))];
text(length(trainAccuracy), trainAccuracy(end) + 0.005*max(trainAccuracy), acuracia_text, 'HorizontalAlignment', 'right', 'Color', 'k');

% Print das métricas gerais
disp('Métricas Gerais:');
disp(['Acurácia Geral: ', num2str(overall_accuracy)]);
disp(['Sensibilidade Geral: ', num2str(overall_sensitivity)]);
disp(['Especificidade Geral: ', num2str(overall_specificity)]);

% Parar o cronômetro e calcular o tempo de execução
execution_time = toc;
disp(['Tempo de execução: ', num2str(execution_time), ' segundos']);
