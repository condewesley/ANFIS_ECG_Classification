Pré-processamento dos Dados em Python
O primeiro estágio do projeto envolveu o pré-processamento dos dados utilizando Python. Inicialmente, os dados brutos do banco de dados MIT-BIH foram filtrados para selecionar apenas os tipos específicos de batimentos cardíacos de interesse: Normal (N), Batimento Atrial Prematuro (A), Bloqueio do Ramo Direito (R), Bloqueio do Ramo Esquerdo (L) e Batimento de Marca-Passo (). Durante essa fase, foram aplicados filtros para eliminar ruídos e artefatos dos sinais de ECG.

Além disso, as anotações dos batimentos cardíacos foram analisadas e selecionadas cuidadosamente para garantir que apenas os batimentos desejados fossem incluídos no conjunto de dados final. Esse processo foi crucial para garantir a qualidade e a relevância dos dados utilizados nas etapas subsequentes do projeto.

Criação e Treinamento do Modelo ANFIS em MATLAB
Após o pré-processamento e a seleção dos batimentos cardíacos específicos em Python, os dados foram importados para o MATLAB, onde o modelo ANFIS (Adaptive Neuro-Fuzzy Inference System) foi criado e treinado. O MATLAB foi escolhido por sua robustez e eficiência no desenvolvimento de sistemas de inferência neuro-fuzzy.

No MATLAB, a função genfis foi utilizada para gerar o Sistema Fuzzy Inicial (FIS) através do método de clustering subtrativo. Esse método de particionamento é amplamente utilizado para criar partições difusas a partir dos dados de entrada, onde os centros dos clusters são determinados com base na densidade dos dados. O valor do raio de influência foi ajustado para 0.7, garantindo um equilíbrio razoável entre a interpretabilidade das regras e a eficácia dos resultados de classificação.

O modelo ANFIS foi treinado utilizando 800 épocas, um número definido como critério de parada para garantir um treinamento adequado sem overfitting. Durante o treinamento, os dados foram divididos em conjuntos de treinamento, validação e teste na proporção de 70%, 15% e 15%, respectivamente. Este processo iterativo ajustou os parâmetros do sistema até que o erro mínimo de validação fosse alcançado.

Após a conclusão do treinamento, o modelo foi testado para verificar sua precisão e eficácia na classificação de batimentos cardíacos. As métricas de desempenho, incluindo acurácia, sensibilidade e especificidade, foram calculadas para avaliar a eficácia do sistema.
