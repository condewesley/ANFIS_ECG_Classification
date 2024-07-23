% Definir a frequência de amostragem (Fs)
Fs = 360;

% Número total de sinais no conjunto de teste
num_signals_test = size(Test, 1);

% Inicialização da matriz para armazenar características de todos os sinais de teste
Input_Test_All = zeros(num_signals_test, 11); % Agora com espaço para 11 características

% Processamento de cada sinal de teste
for signal_id_test = 1:num_signals_test
    % Extrair sinal de ECG
    ecgsig_test = Test(signal_id_test, 1:1080);
    
    % Calcular transformada wavelet
    wt_test = modwt(ecgsig_test, 6, 'db4');
    
    % Calcular coeficientes de aproximação e detalhe
    a6_test = wt_test(1,:);
    d6_test = wt_test(2,:);
    d5_test = wt_test(3,:);
    d4_test = wt_test(4,:);
    d3_test = wt_test(5,:);
    d2_test = wt_test(6,:);
    d1_test = wt_test(7,:);
    
    % Calcular a energia do sinal
    energy_test = sum(ecgsig_test.^2);
    
    % Inverter DWT para obter o sinal transformado
    wtrec_test = zeros(size(wt_test));
    wtrec_test(3:4, :) = wt_test(3:4, :);
    y_test = imodwt(wtrec_test, 'db4');
    y_test = abs(y_test).^2;
    
    % Calcular picos R
    avg_test = mean(y_test);
    approx_peak_distance_test = round(0.3 * Fs);
    [Rpeaks_test, locs_test] = findpeaks(y_test, 'MinPeakHeight', 5 * avg_test, 'MinPeakDistance', approx_peak_distance_test);
    
    % Calcular intervalos RR
    RR_intervals_test = diff(locs_test) / Fs;
    
    % Calcular o maior, o menor e a soma dos intervalos RR
    max_RR_interval_test = max(RR_intervals_test);
    min_RR_interval_test = min(RR_intervals_test);
    mean_RR_interval_test = mean(RR_intervals_test);
    sum_RR_intervals_test = sum(RR_intervals_test);
    
    % Calcular características do sinal
    R_amplitude_test = max(ecgsig_test);
    min_signal_test = min(ecgsig_test);
    mean_signal_test = mean(ecgsig_test);
    std_signal_test = std(ecgsig_test);
    dp_rr_test = std(RR_intervals_test);
    
    % Tipo de sinal
    signal_type_test = Test(signal_id_test, 1081);
    
    % Quantidade de batimentos cardíacos
    num_beats_test = length(locs_test);
    
    % Calcular a duração total do sinal ECG em segundos
    T_test = length(ecgsig_test) / Fs;

    % Calcular a taxa média de batimentos cardíacos
    hbpermin_alternative_test = (num_beats_test / T_test) * 60;
    
    % Salvar características na matriz
    Input_Test_All(signal_id_test, :) = [R_amplitude_test, min_signal_test, energy_test, mean_signal_test, std_signal_test, dp_rr_test, num_beats_test, max_RR_interval_test, min_RR_interval_test, mean_RR_interval_test, signal_type_test];

    % Plotar sinal original e transformado apenas para o primeiro sinal
    if signal_id_test == 1
        % Time vector for 3 seconds
        t_3s_test = (1:3*Fs) / Fs;

        % Displaying ECG signal and detected R-Peaks
        figure
        subplot(411)
        plot(t_3s_test, ecgsig_test);
        xlim([0, 3]);
        grid on;
        xlabel('Seconds')
        title('Original ECG Signal (Test)')
        
        % Plotar coeficientes da transformada wavelet
        subplot(412)
        plot(t_3s_test, a6_test(1:length(t_3s_test)), 'r') % Aproximação
        hold on
        plot(t_3s_test, d6_test(1:length(t_3s_test)), 'b') % Detalhes
        plot(t_3s_test, d5_test(1:length(t_3s_test)), 'g')
        plot(t_3s_test, d4_test(1:length(t_3s_test)), 'm')
        plot(t_3s_test, d3_test(1:length(t_3s_test)), 'y')
        plot(t_3s_test, d2_test(1:length(t_3s_test)), 'c')
        plot(t_3s_test, d1_test(1:length(t_3s_test)), 'k')
        title('Wavelet Coefficients (Test)')
        xlabel('Seconds')
        legend('a6', 'd6', 'd5', 'd4', 'd3', 'd2', 'd1')
        
        % Plotar apenas os coeficientes escolhidos para transformar o sinal
        subplot(413)
        plot(t_3s_test, d5_test(1:length(t_3s_test)), 'g')
        hold on
        plot(t_3s_test, d4_test(1:length(t_3s_test)), 'm')
        title('Selected Wavelet Coefficients (Test)')
        xlabel('Seconds')
        legend('d5', 'd4')

        subplot(414)
        plot(t_3s_test, y_test)
        grid on;
        xlim([0, 3]);
        hold on
        plot(locs_test/Fs, Rpeaks_test, 'ro', 'MarkerSize', 5) % Added red circular markers
        xlabel('Seconds')
        title(['Transformed Signal with R Peaks and Heart Rate (Test): ', num2str(hbpermin_alternative_test)])
    end
end
