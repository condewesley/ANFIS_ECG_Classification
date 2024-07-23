% Selecionando as colunas relevantes
dados = Input_Train_All(:, [1, 5, 6, 8, 9]);
tipos = Input_Train_All(:, 11);

% Mapeando os tipos para seus respectivos nomes
nomes_tipos = {'Ritmo Sinusal Normal (NSR)', 'Contração Atrial Prematura (PAC)', 'Bloqueio do Ramo Direito (RBBB)', ...
             'Bloqueio do Ramo Esquerdo (LBBB)', 'Batimento com Marca-Passo (PB)'};

% Nomes das entradas
nomes_entradas = {'Amplitude do Pico R', 'Desvio Padrão do Sinal ECG', 'Desvio Padrão dos Intervalos RR', ...
             'Maior Intervalo RR', 'Menor Intervalo RR'};

% Criando a figura para cada entrada
for entrada = 1:5
    % Criando a figura para cada entrada
    figure('Name', ['Distribuição de ', nomes_entradas{entrada}]);
    
    % Loop através de cada tipo de ritmo cardíaco
    for tipo = 1:5
        % Selecionando os dados correspondentes ao tipo atual e à entrada atual
        dados_tipo_i = dados(tipos == tipo, entrada); 
        
        % Definindo a posição do subplot
        subplot(2, 3, tipo);
        
        % Plotando o histograma com estilo personalizado
        histogram(dados_tipo_i, 'FaceColor', [0.7 0.7 0.7], 'EdgeColor', 'k', 'FaceAlpha', 1.0);
        hold on;
        
        % Ajustando uma distribuição normal (gaussiana) aos dados
        pd = fitdist(dados_tipo_i, 'Normal');
    
        % Calculando os valores da curva gaussiana
        x_values = linspace(min(dados_tipo_i), max(dados_tipo_i), 100);
        y_values = pdf(pd, x_values);
    
        % Plotando a curva gaussiana
        plot(x_values, y_values, 'r', 'LineWidth', 2);
    
        % Calculando e marcando a média da curva gaussiana
        media_gaussiana = mean(pd);
        plot(media_gaussiana, pdf(pd, media_gaussiana), 'ro', 'MarkerSize', 6, 'MarkerFaceColor', 'r');
        text(media_gaussiana, pdf(pd, media_gaussiana), ['\bf Média: ', num2str(media_gaussiana)], 'VerticalAlignment', 'bottom');
        
        % Adicionando rótulo ao eixo x
        xlabel(nomes_entradas{entrada});
        
        % Adicionando título e rótulos
        title(nomes_tipos{tipo});
        ylabel('Frequência');
    end
end
