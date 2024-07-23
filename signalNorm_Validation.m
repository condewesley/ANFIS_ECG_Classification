% Definir a frequência de amostragem (Fs)
Fs = 360;

% Número total de sinais no conjunto de treinamento
num_signals_validation = size(Validation, 1);

% Inicialização da matriz para armazenar características de todos os sinais de validação
Input_Validation_All = zeros(num_signals_validation, 11); % Agora com espaço para 11 características

% Processamento de cada sinal de validação
for signal_id_validation = 1:num_signals_validation
    % Extrair sinal de ECG
    ecgsig_validation = Validation(signal_id_validation, 1:1080);
    
    % Calcular transformada wavelet
    wt_validation = modwt(ecgsig_validation, 6, 'db4');
    
    % Calcular coeficientes de aproximação e detalhe
    a6_validation = wt_validation(1,:);
    d6_validation = wt_validation(2,:);
    d5_validation = wt_validation(3,:);
    d4_validation = wt_validation(4,:);
    d3_validation = wt_validation(5,:);
    d2_validation = wt_validation(6,:);
    d1_validation = wt_validation(7,:);
    
    % Calcular a energia do sinal
    energy_validation = sum(ecgsig_validation.^2);
    
    % Inverter DWT para obter o sinal transformado
    wtrec_validation = zeros(size(wt_validation));
    wtrec_validation(3:4, :) = wt_validation(3:4, :);
    y_validation = imodwt(wtrec_validation, 'db4');
    y_validation = abs(y_validation).^2;
    
    % Calcular picos R
    avg_validation = mean(y_validation);
    approx_peak_distance_validation = round(0.3 * Fs);
    [Rpeaks_validation, locs_validation] = findpeaks(y_validation, 'MinPeakHeight', 5 * avg_validation, 'MinPeakDistance', approx_peak_distance_validation);
    
    % Calcular intervalos RR
    RR_intervals_validation = diff(locs_validation) / Fs;
    
    % Calcular o maior, o menor e a soma dos intervalos RR
    max_RR_interval_validation = max(RR_intervals_validation);
    min_RR_interval_validation = min(RR_intervals_validation);
    mean_RR_interval_validation = mean(RR_intervals_validation);
    sum_RR_intervals_validation = sum(RR_intervals_validation);
    
    % Calcular características do sinal
    R_amplitude_validation = max(ecgsig_validation);
    min_signal_validation = min(ecgsig_validation);
    mean_signal_validation = mean(ecgsig_validation);
    std_signal_validation = std(ecgsig_validation);
    dp_rr_validation = std(RR_intervals_validation);
    
    % Tipo de sinal
    signal_type_validation = Validation(signal_id_validation, 1081);
    
    % Quantidade de batimentos cardíacos
    num_beats_validation = length(locs_validation);
    
    % Calcular a duração total do sinal ECG em segundos
    T_validation = length(ecgsig_validation) / Fs;

    % Calcular a taxa média de batimentos cardíacos
    hbpermin_alternative_validation = (num_beats_validation / T_validation) * 60;
    
    % Salvar características na matriz
    Input_Validation_All(signal_id_validation, :) = [R_amplitude_validation, min_signal_validation, energy_validation, mean_signal_validation, std_signal_validation, dp_rr_validation, num_beats_validation, max_RR_interval_validation, min_RR_interval_validation, mean_RR_interval_validation, signal_type_validation];

    % Plotar sinal original e transformado apenas para o primeiro sinal
    if signal_id_validation == 1
        % Time vector for 3 seconds
        t_3s_validation = (1:3*Fs) / Fs;

        % Displaying ECG signal and detected R-Peaks
        figure
        subplot(411)
        plot(t_3s_validation, ecgsig_validation);
        xlim([0, 3]);
        grid on;
        xlabel('Seconds')
        title('Original ECG Signal (Validation)')
        
        % Plotar coeficientes da transformada wavelet
        subplot(412)
        plot(t_3s_validation, a6_validation(1:length(t_3s_validation)), 'r') % Aproximação
        hold on
        plot(t_3s_validation, d6_validation(1:length(t_3s_validation)), 'b') % Detalhes
        plot(t_3s_validation, d5_validation(1:length(t_3s_validation)), 'g')
        plot(t_3s_validation, d4_validation(1:length(t_3s_validation)), 'm')
        plot(t_3s_validation, d3_validation(1:length(t_3s_validation)), 'y')
        plot(t_3s_validation, d2_validation(1:length(t_3s_validation)), 'c')
        plot(t_3s_validation, d1_validation(1:length(t_3s_validation)), 'k')
        title('Wavelet Coefficients (Validation)')
        xlabel('Seconds')
        legend('a6', 'd6', 'd5', 'd4', 'd3', 'd2', 'd1')
        
        % Plotar apenas os coeficientes escolhidos para transformar o sinal
        subplot(413)
        plot(t_3s_validation, d5_validation(1:length(t_3s_validation)), 'g')
        hold on
        plot(t_3s_validation, d4_validation(1:length(t_3s_validation)), 'm')
        title('Selected Wavelet Coefficients (Validation)')
        xlabel('Seconds')
        legend('d5', 'd4')

        subplot(414)
        plot(t_3s_validation, y_validation)
        grid on;
        xlim([0, 3]);
        hold on
        plot(locs_validation/Fs, Rpeaks_validation, 'ro', 'MarkerSize', 5) % Added red circular markers
        xlabel('Seconds')
        title(['Transformed Signal with R Peaks and Heart Rate (Validation): ', num2str(hbpermin_alternative_validation)])
    end
end
