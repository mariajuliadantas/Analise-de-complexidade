Análise de Desempenho do HeapSort (C vs. Python)

Este projeto realiza uma análise de benchmark comparando os tempos de execução de implementações do algoritmo HeapSort em C (uma linguagem compilada) e Python (uma linguagem interpretada).

O objetivo é medir o tempo de execução para entradas de diferentes tamanhos (pequena, média, grande) e comparar os resultados práticos com a complexidade teórica esperada do algoritmo, que é $\Theta(n \log n)$.

Estrutura do Projeto

heap.c: Implementação do HeapSort em C. Contém a lógica de benchmarking para rodar o algoritmo N vezes e calcular média e desvio padrão.

heap.py: Implementação do HeapSort em Python. Também contém a lógica de benchmarking.

gerar_graficos.py: Script Python (requer matplotlib e numpy) que contém os dados de resultado (coletados dos scripts .c e .py) e gera os gráficos de análise visual.

Nota: Os dados dos benchmarks estão "hardcoded" (fixos) dentro do arquivo gerar_graficos.py para fins de reprodutibilidade da visualização. Os arquivos .c e .py estão incluídos como a fonte original desses dados.

Como Reproduzir

Pré-requisitos:

Python 3

Bibliotecas: pip install matplotlib numpy

Gerar os Gráficos:
Para gerar os gráficos de análise a partir dos dados coletados, execute:

python gerar_graficos.py



Isso salvará três imagens PNG no diretório.

(Opcional) Executar os Benchmarks Originais:
Se desejar rodar os benchmarks você mesmo:

Python: python heap.py

C: gcc heap.c -o heap_c_exec -lm (para compilar) e depois ./heap_c_exec (para rodar)

Resultados da Análise

Os gráficos abaixo foram gerados pelos scripts deste repositório.

1. Desempenho do HeapSort (C vs. Python)

Análise: Este gráfico mostra o tempo médio de execução em escala logarítmica. Confirma-se que:

Ambas as linguagens seguem uma curva de crescimento superlinear, consistente com a complexidade $\Theta(n \log n)$.

A implementação em C é ordens de magnitude mais rápida que a de Python em todas as entradas.

2. Fator de Aceleração (C vs. Python)

Análise: Este gráfico quantifica a diferença de velocidade. A versão em C é consistentemente entre 16x e 24x mais rápida que a versão em Python, com a diferença se estabilizando em torno de 19.4x para entradas grandes.

3. Análise de Complexidade Teórica

Análise: Este é o gráfico de validação mais importante. Ao normalizar o tempo de execução $T(n)$ dividindo-o por $n \log n$, esperamos obter uma constante $c$.

As linhas quase horizontais para C e Python provam empiricamente que o tempo de execução escala de acordo com a complexidade teórica $\Theta(n \log n)$.
