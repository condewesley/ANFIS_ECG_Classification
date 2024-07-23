% Definir a frequência de amostragem (Fs)
Fs = 360;

% Número total de sinais no conjunto de treinamento
num_signals_train = size(Train, 1);

% Inicialização da matriz para armazenar características de todos os sinais de treinamento
Input_Train_All = zeros(num_signals_train, 11); % Agora com espaço para 11 características

% Processamento de cada sinal de treinamento
for signal_id_train = 1:num_signals_train
    % Extrair sinal de ECG
    ecgsig_train = Train(signal_id_train, 1:1080);
    
    % Calcular picos R antes da transformada wavelet
    avg_train_original = mean(ecgsig_train);
    approx_peak_distance_train_original = round(0.3 * Fs);
    [Rpeaks_train_original, locs_train_original] = findpeaks(ecgsig_train, 'MinPeakHeight', 5 * avg_train_original, 'MinPeakDistance', approx_peak_distance_train_original);
    
    % Calcular transformada wavelet
    wt_train = modwt(ecgsig_train, 6, 'db4');
    
    % Calcular coeficientes de aproximação e detalhe
    a6_train = wt_train(1,:);
    d6_train = wt_train(2,:);
    d5_train = wt_train(3,:);
    d4_train = wt_train(4,:);
    d3_train = wt_train(5,:);
    d2_train = wt_train(6,:);
    d1_train = wt_train(7,:);
    
    % Calcular a energia do sinal
    energy_train = sum(ecgsig_train.^2);
    
    % Inverter DWT para obter o sinal transformado
    wtrec_train = zeros(size(wt_train));
    wtrec_train(3:4, :) = wt_train(3:4, :);
    y_train = imodwt(wtrec_train, 'db4');
    y_train = abs(y_train).^2;
    
    % Calcular picos R após a transformada wavelet
    avg_train = mean(y_train);
    approx_peak_distance_train = round(0.3 * Fs);
    [Rpeaks_train, locs_train] = findpeaks(y_train, 'MinPeakHeight', 5 * avg_train, 'MinPeakDistance', approx_peak_distance_train);
    
    % Calcular intervalos RR
    RR_intervals_train = diff(locs_train) / Fs;
    
    % Calcular o maior, o menor e a soma dos intervalos RR
    max_RR_interval_train = max(RR_intervals_train);
    min_RR_interval_train = min(RR_intervals_train);
    mean_RR_interval_train = mean(RR_intervals_train);
    sum_RR_intervals_train = sum(RR_intervals_train);
    
    % Calcular características do sinal
    R_amplitude_train = max(ecgsig_train);
    min_signal_train = min(ecgsig_train);
    mean_signal_train = mean(ecgsig_train);
    std_signal_train = std(ecgsig_train);
    dp_rr_train = std(RR_intervals_train);
    
    % Tipo de sinal
    signal_type_train = Train(signal_id_train, 1081);
    
    % Quantidade de batimentos cardíacos
    num_beats_train = length(locs_train);
    
    % Calcular a duração total do sinal ECG em segundos
    T_train = length(ecgsig_train) / Fs;

    % Calcular a taxa média de batimentos cardíacos
    hbpermin_alternative_train = (num_beats_train / T_train) * 60;
    
    % Salvar características na matriz
    Input_Train_All(signal_id_train, :) = [R_amplitude_train, min_signal_train, energy_train, mean_signal_train, std_signal_train, dp_rr_train, num_beats_train, max_RR_interval_train, min_RR_interval_train, mean_RR_interval_train, signal_type_train];

    % Plotar sinal original e transformado apenas para o primeiro sinal
    if signal_id_train == 1
        % Time vector for 3 seconds
        t_3s_train = (1:3*Fs) / Fs;

        % Plotar sinal ECG original
        figure
        subplot(511)
        plot(t_3s_train, ecgsig_train);
        xlim([0, 3]);
        grid on;
        xlabel('Segundos')
        ylabel('Amplitude (mV)')
        title('Original ECG Signal (Train)')

        % Displaying ECG signal and detected R-Peaks before wavelet transform
        subplot(512)
        plot(t_3s_train, ecgsig_train);
        hold on;
        plot(locs_train_original/Fs, Rpeaks_train_original, 'ro', 'MarkerSize', 5) % Added red circular markers
        xlim([0, 3]);
        grid on;
        xlabel('Segundos')
        ylabel('Amplitude (mV)')
        title('Original ECG Signal with R Peaks (Train)')
        
        % Plotar coeficientes da transformada wavelet
        subplot(513)
        plot(t_3s_train, a6_train(1:length(t_3s_train)), 'r') % Aproximação
        hold on
        plot(t_3s_train, d6_train(1:length(t_3s_train)), 'b') % Detalhes
        plot(t_3s_train, d5_train(1:length(t_3s_train)), 'g')
        plot(t_3s_train, d4_train(1:length(t_3s_train)), 'm')
        plot(t_3s_train, d3_train(1:length(t_3s_train)), 'y')
        plot(t_3s_train, d2_train(1:length(t_3s_train)), 'c')
        plot(t_3s_train, d1_train(1:length(t_3s_train)), 'k')
        title('Wavelet Coefficients (Train)')
        xlabel('Segundos')
        ylabel('Amplitude (mV)')
        legend('a6', 'd6', 'd5', 'd4', 'd3', 'd2', 'd1')
        
        % Plotar apenas os coeficientes escolhidos para transformar o sinal
        subplot(514)
        plot(t_3s_train, d5_train(1:length(t_3s_train)), 'g')
        hold on
        plot(t_3s_train, d4_train(1:length(t_3s_train)), 'm')
        title('Selected Wavelet Coefficients (Train)')
        xlabel('Segundos')
        ylabel('Amplitude (mV)')
        legend('d5', 'd4')

        % Displaying ECG signal and detected R-Peaks after wavelet transform
        subplot(515)
        plot(t_3s_train, y_train)
        grid on;
        xlim([0, 3]);
        hold on
        plot(locs_train/Fs, Rpeaks_train, 'ro', 'MarkerSize', 5) % Added red circular markers
        xlabel('Segundos')
        ylabel('Amplitude (mV)')
        title(['Transformed Signal with R Peaks and Heart Rate (Train): ', num2str(hbpermin_alternative_train)])
    end
end
