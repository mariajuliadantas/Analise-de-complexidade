import matplotlib.pyplot as plt
import numpy as np

# --- 1. Dados Extraídos do Benchmark ---
# Estes são os dados que você forneceu, já resumidos.

labels = ['Pequeno (1k)', 'Médio (10k)', 'Grande (100k)']
tamanhos_n = [1000, 10000, 100000]

# Dados do Python
python_medias = [0.003954, 0.030530, 0.446888]
python_desvios = [0.006136, 0.003250, 0.021328]

# Dados do C
c_medias = [0.000167, 0.001900, 0.023067]
c_desvios = [0.000373, 0.000651, 0.001504]


# --- 2. Gráfico 1: Comparação de Desempenho (Log Scale) ---

# Cria a primeira figura
plt.figure(figsize=(10, 6))

# Plot Python (com barras de erro/desvio padrão)
plt.errorbar(labels, python_medias, yerr=python_desvios, 
             marker='o', capsize=5, linestyle='-', label='Python')

# Plot C (com barras de erro/desvio padrão)
plt.errorbar(labels, c_medias, yerr=c_desvios, 
             marker='s', capsize=5, linestyle='--', label='C')

# !! IMPORTANTE: Usar escala logarítmica !!
# Os valores de C (ex: 0.000167s) são tão menores que os do Python (ex: 0.44s)
# que eles desapareceriam em uma escala linear. A escala logarítmica
# nos permite ver e comparar ambas as curvas de crescimento.
plt.yscale('log')

# Configurações do Gráfico
plt.title('Desempenho do HeapSort (C vs. Python)', fontsize=16)
plt.xlabel('Tamanho da Entrada (N)', fontsize=12)
plt.ylabel('Tempo Médio (segundos) - Escala Logarítmica', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5) # Grid para ambas as escalas (major/minor)
plt.tight_layout() # Ajusta layout para não cortar os rótulos

# Salvar o gráfico em um arquivo
plt.savefig('grafico_comparacao_log.png', dpi=300)
print("Gráfico 'grafico_comparacao_log.png' salvo com sucesso.")


# --- 3. Gráfico 2: Fator de Aceleração (Speed-up) ---

# Converter para arrays numpy para facilitar a divisão
py_medias_np = np.array(python_medias)
c_medias_np = np.array(c_medias)

# Calcular quantas vezes C foi mais rápido (Média Python / Média C)
speedup = py_medias_np / c_medias_np

# Cria a segunda figura
plt.figure(figsize=(8, 5))
bars = plt.bar(labels, speedup, color='teal', 
               edgecolor='black', width=0.6)

# Adicionar o valor (ex: "23.7x") em cima de cada barra
plt.bar_label(bars, fmt='%.1fx', fontsize=12, padding=3)

# Configurações do Gráfico
plt.title('Fator de Aceleração (C vs. Python)', fontsize=16)
plt.xlabel('Tamanho da Entrada', fontsize=12)
plt.ylabel('Aceleração (Média Python / Média C)', fontsize=12)
plt.ylim(0, max(speedup) * 1.2) # Dá um espaço extra no topo
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Salvar o segundo gráfico
plt.savefig('grafico_speedup.png', dpi=300)
print("Gráfico 'grafico_speedup.png' salvo com sucesso.")


# --- 4. Gráfico 3: Comprovação da Complexidade Teórica ---
# Este gráfico valida se o tempo medido T(n) segue a complexidade 
# teórica O(n*log(n)). Se T(n) ≈ c * n*log(n), então T(n)/(n*log(n)) ≈ c.
# Uma linha horizontal (ou quase) comprova a teoria.

# (py_medias_np e c_medias_np já foram criados para o Gráfico 2)
n_array = np.array(tamanhos_n)

# Calcular n * log(n)
n_log_n = n_array * np.log(n_array)

# Normalizar os tempos: T(n) / (n * log(n))
# (Adicionamos uma verificação de segurança para c_medias_np caso seja 0)
safe_c_medias = np.where(c_medias_np == 0, 1e-12, c_medias_np) 
py_normalizado = py_medias_np / n_log_n
c_normalizado = safe_c_medias / n_log_n

# Cria a terceira figura
plt.figure(figsize=(10, 6))

plt.plot(labels, py_normalizado, marker='o', linestyle='-', label='Python (Constante "c")')
plt.plot(labels, c_normalizado, marker='s', linestyle='--', label='C (Constante "c")')

# Configurações do Gráfico
plt.title('Análise de Complexidade Teórica (Tempo Normalizado)', fontsize=16)
plt.xlabel('Tamanho da Entrada (N)', fontsize=12)
plt.ylabel('Tempo Normalizado ( T(n) / (N*log(N)) )', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.yscale('log') 
plt.tight_layout()

# Salvar o terceiro gráfico
plt.savefig('grafico_complexidade_teorica.png', dpi=300)
print("Salvo: 'grafico_complexidade_teorica.png'")


# --- 5. Exibir os gráficos ---
print("Exibindo gráficos (feche as janelas para terminar)...")
plt.show()