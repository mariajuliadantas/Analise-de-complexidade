import time
import random
import numpy as np
import sys

# Aumenta o limite de recursão para heaps grandes
sys.setrecursionlimit(200000)

# Função recursiva central
def heapify(arr, N, i):
    """
    Garante a propriedade de Max-Heap a partir do nó i.
    N é o tamanho do heap (pode ser menor que o array).
    i é o índice da raiz (onde começamos o peneiramento).
    """
    maior = i       # Inicializa o maior como a raiz
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Verifica se o filho da esquerda existe e é maior que a raiz
    if esquerda < N and arr[esquerda] > arr[maior]:
        maior = esquerda

    # Verifica se o filho da direita existe e é maior que o 'maior' atual
    if direita < N and arr[direita] > arr[maior]:
        maior = direita

    # Se 'maior' não for mais a raiz, troca e chama recursivamente
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]  # Troca
        # Chama recursivamente para a sub-árvore afetada
        heapify(arr, N, maior)

# Função principal do HeapSort
def heapSort(arr):
    N = len(arr)

    # 1. Construir o Max-Heap
    # Começa do último nó que NÃO é folha e vai até a raiz
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    # 2. Extrair elementos um por um
    for i in range(N - 1, 0, -1):
        # Move a raiz atual (maior) para o fim
        arr[i], arr[0] = arr[0], arr[i]
        # Chama o heapify na raiz do heap reduzido (tamanho 'i')
        heapify(arr, i, 0)

# --- Seção de Benchmarking ---

def run_benchmark(size, num_runs):
    """
    Roda o benchmark para um tamanho de entrada (size)
    por 'num_runs' vezes.
    """
    times = []
    print(f"\n--- Iniciando Benchmark: {size} elementos ({num_runs} execuções) ---")

    for i in range(num_runs):
        # Gera dados sintéticos (números aleatórios de 0 a 10*size)
        # Usamos uma cópia para não ordenar o array já ordenado na próxima iteração
        original_array = [random.randint(0, size * 10) for _ in range(size)]
        
        # Copia os dados para a ordenação não afetar a próxima rodada
        arr_to_sort = original_array.copy()

        start_time = time.perf_counter() # Medidor de tempo de alta precisão
        
        heapSort(arr_to_sort)
        
        end_time = time.perf_counter()
        
        exec_time = end_time - start_time
        times.append(exec_time)
        
        # Exibe o tempo de cada execução individual
        print(f"  Execução {i+1}/{num_runs}: {exec_time:.6f} segundos")

    # Calcula estatísticas
    mean_time = np.mean(times)
    std_dev = np.std(times)

    print("-" * (30 + len(str(size))))
    print(f"Resultados para {size} elementos:")
    print(f"  Tempo Médio:   {mean_time:.6f} segundos")
    print(f"  Desvio Padrão: {std_dev:.6f} segundos")
    print("-" * (30 + len(str(size))))
    return mean_time, std_dev

# Definição das entradas
N_PEQUENO = 1000
N_MEDIO = 10000
N_GRANDE = 100000
N_EXECUCOES = 30 # Você pode mudar para 15 ou 30

if __name__ == "__main__":
    print("Iniciando Simulação (Python)...")
    
    # Dicionário para guardar resultados
    resultados = {}

    # Rodar simulações
    resultados["Pequeno"] = run_benchmark(N_PEQUENO, N_EXECUCOES)
    resultados["Médio"] = run_benchmark(N_MEDIO, N_EXECUCOES)
    resultados["Grande"] = run_benchmark(N_GRANDE, N_EXECUCOES)

    print("\n\n--- 📊 Resumo Final (Python) ---")
    print(f"{'Tamanho':<10} | {'Média (s)':<15} | {'Desvio Padrão (s)':<20}")
    print("-" * 50)
    print(f"{'Pequeno':<10} | {resultados['Pequeno'][0]:<15.6f} | {resultados['Pequeno'][1]:<20.6f}")
    print(f"{'Médio':<10} | {resultados['Médio'][0]:<15.6f} | {resultados['Médio'][1]:<20.6f}")
    print(f"{'Grande':<10} | {resultados['Grande'][0]:<15.6f} | {resultados['Grande'][1]:<20.6f}")