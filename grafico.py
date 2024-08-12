import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

files = glob.glob('similaridade/*.csv')
files.sort()

# Definir o número de colunas e linhas
num_cols = 3
num_rows = 3
fig, axs = plt.subplots(num_rows, num_cols, figsize=(18, 12))

# Flatten the axs array for easy iteration if there's more than one row
axs = axs.flatten()
nomes = list()
for file in files:
    nome = file.split('/')[1].split('.')[0].split('s')[0].split('_')[0].upper()
    nomes.append(nome)

# Iterar sobre os arquivos e os subplots
for i, file in enumerate(files):
    if i == 6:
        i = 7
    df = pd.read_csv(file)
    df.sort_values(by='Variante',inplace=True)
    print(df)
    nomes_labels = list()
    nomes_labels = nomes.copy()
    nome_variante = file.split('/')[1].split('.')[0].split('s')[0].split('_')[0].upper()
    nomes_labels.remove(nome_variante)
    for Index, nome in enumerate(nomes_labels):
        nomes_labels[Index] = nome + ' SZZ'
    print(nomes_labels)
    # Criar o gráfico de barras no subplot correspondente
    bars = axs[i].bar(df['Variante'], df['Similaridade'], color=sns.color_palette("ch:s=.25,rot=-.25", n_colors=len(df)))

    # Adicionar os valores no topo de cada barra
    for bar in bars:
        height = bar.get_height()
        axs[i].text(
            bar.get_x() + bar.get_width() / 2,  # Posição X do texto
            height,  # Posição Y do texto (topo da barra)
            f'{height:.1f}%',  # Texto (valor com duas casas decimais)
            ha='center',  # Centralizar o texto horizontalmente
            va='bottom'   # Alinhar o texto à base do topo da barra
        )
    
    axs[i].set_xticks(np.arange(len(df['Variante'])))  # Definir a posição dos ticks no eixo X
    axs[i].set_xticklabels(nomes_labels , ha='right')  # Definir os rótulos do eixo X
    # Definir rótulos e título para o subplot atual
    axs[i].set_ylabel('Similaridade (%)')
    axs[i].set_title('Porcentagem de Rótulos Iguais ao ' + nome_variante + ' SZZ')
    axs[i].set_ylim(0, 106)  # Definir o intervalo do eixo Y
    
# Garantir que o último gráfico da segunda linha está na última coluna
# Se houver menos gráficos do que subplots, remover os subplots extras
for j in range(i + 1, len(axs)):
    fig.delaxes(axs[j])
fig.delaxes(axs[6])
# Ajustar o layout para evitar sobreposição
plt.tight_layout()

# Mostrar o gráfico com todos os subplots organizados
plt.savefig('similaridade/similaridade.eps',format='eps')
plt.show()
