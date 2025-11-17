#include <stdio.h>
#include <stdlib.h> // Para malloc, free, rand
#include <time.h>   // Para clock()
#include <math.h>   // Para sqrt() (desvio padrão)

// Função helper para trocar dois inteiros
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// A FUNÇÃO RECURSIVA: Garante a propriedade de Max-Heap
// N é o tamanho do heap
// i é o índice da raiz
void heapify(int arr[], int N, int i) {
    int maior = i;       // Inicializa o maior como a raiz
    int esquerda = 2 * i + 1;
    int direita = 2 * i + 2;

    // Verifica se o filho da esquerda existe e é maior que a raiz
    if (esquerda < N && arr[esquerda] > arr[maior])
        maior = esquerda;

    // Verifica se o filho da direita existe e é maior que o 'maior' atual
    if (direita < N && arr[direita] > arr[maior])
        maior = direita;

    // Se 'maior' não for mais a raiz, troca e chama recursivamente
    if (maior != i) {
        swap(&arr[i], &arr[maior]);
        // Chama recursivamente para a sub-árvore afetada
        heapify(arr, N, maior);
    }
}

// Função principal do HeapSort
void heapSort(int arr[], int N) {
    // 1. Construir o Max-Heap (reorganizar o array)
    // Começa do último nó que NÃO é folha e vai até a raiz
    for (int i = N / 2 - 1; i >= 0; i--)
        heapify(arr, N, i);

    // 2. Extrair elementos um por um do heap
    for (int i = N - 1; i > 0; i--) {
        // Move a raiz atual (maior) para o fim
        swap(&arr[0], &arr[i]);

        // Chama o heapify na raiz do heap reduzido (tamanho 'i')
        heapify(arr, i, 0);
    }
}

// --- Seção de Benchmarking ---

// Estrutura para guardar os resultados estatísticos
typedef struct {
    double media;
    double desvio_padrao;
} Stats;

// Calcula média e desvio padrão
Stats calcular_stats(double tempos[], int num_runs) {
    double soma = 0.0;
    for (int i = 0; i < num_runs; i++) {
        soma += tempos[i];
    }
    double media = soma / num_runs;

    double soma_diff_quad = 0.0;
    for (int i = 0; i < num_runs; i++) {
        soma_diff_quad += pow(tempos[i] - media, 2);
    }
    double desvio_padrao = sqrt(soma_diff_quad / num_runs);

    Stats resultados = {media, desvio_padrao};
    return resultados;
}

// Roda o benchmark
Stats run_benchmark(int size, int num_runs) {
    double* times = (double*)malloc(num_runs * sizeof(double));
    if (times == NULL) {
        printf("Falha ao alocar memória para tempos.\n");
        exit(1);
    }

    printf("\n--- Iniciando Benchmark: %d elementos (%d execuções) ---\n", size, num_runs);

    for (int i = 0; i < num_runs; i++) {
        // Alocar memória para o array de dados
        int* arr = (int*)malloc(size * sizeof(int));
        if (arr == NULL) {
            printf("Falha ao alocar memória para o array.\n");
            exit(1);
        }

        // Gerar dados sintéticos
        // (Usamos uma cópia do array original se fôssemos reutilizá-lo,
        // mas aqui é mais fácil gerar um novo a cada vez)
        for (int j = 0; j < size; j++) {
            arr[j] = rand() % (size * 10);
        }

        clock_t start = clock(); // Inicia medidor de tempo
        
        heapSort(arr, size);
        
        clock_t end = clock();   // Finaliza medidor de tempo

        double exec_time = ((double)(end - start)) / CLOCKS_PER_SEC;
        times[i] = exec_time;

        printf("  Execução %d/%d: %.6f segundos\n", i + 1, num_runs, exec_time);

        // Liberar memória do array desta iteração
        free(arr);
    }

    // Calcular estatísticas
    Stats resultados = calcular_stats(times, num_runs);
    free(times); // Liberar memória dos tempos

    printf("---------------------------------------------\n");
    printf("Resultados para %d elementos:\n", size);
    printf("  Tempo Médio:   %.6f segundos\n", resultados.media);
    printf("  Desvio Padrão: %.6f segundos\n", resultados.desvio_padrao);
    printf("---------------------------------------------\n");
    
    return resultados;
}

// Definição das entradas
#define N_PEQUENO 1000
#define N_MEDIO 10000
#define N_GRANDE 100000
#define N_EXECUCOES 30 // Você pode mudar para 15 ou 30

int main() {
    // Semente para o gerador de números aleatórios
    srand(time(NULL)); 
    
    printf("Iniciando Simulação (C)...\n");

    Stats resultados[3]; // 0=Pequeno, 1=Médio, 2=Grande

    resultados[0] = run_benchmark(N_PEQUENO, N_EXECUCOES);
    resultados[1] = run_benchmark(N_MEDIO, N_EXECUCOES);
    resultados[2] = run_benchmark(N_GRANDE, N_EXECUCOES);

    printf("\n\n--- 📊 Resumo Final (C) ---\n");
    printf("%-10s | %-15s | %-20s\n", "Tamanho", "Média (s)", "Desvio Padrão (s)");
    printf("---------------------------------------------------\n");
    printf("%-10s | %-15.6f | %-20.6f\n", "Pequeno", resultados[0].media, resultados[0].desvio_padrao);
    printf("%-10s | %-15.6f | %-20.6f\n", "Médio", resultados[1].media, resultados[1].desvio_padrao);
    printf("%-10s | %-15.6f | %-20.6f\n", "Grande", resultados[2].media, resultados[2].desvio_padrao);

    return 0;
}