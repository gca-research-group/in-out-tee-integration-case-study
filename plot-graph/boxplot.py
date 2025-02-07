import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import ScalarFormatter

# Carregar os dados dos arquivos CSV
df_in = pd.read_csv('../summarise-results/aggregated-memory-in-results.csv', thousands='.')
df_out = pd.read_csv('../summarise-results/aggregated-memory-out-results.csv', thousands='.')

# Renomear as colunas para incluir médias e desvios padrão
df_in.columns = [
    'Block Size (MB)', 'Allocation_Time_Mean', 'Allocation_Time_Std', 
    'Write_Time_Mean', 'Write_Time_Std', 'Read_Time_Mean', 
    'Read_Time_Std', 'Free_Time_Mean', 'Free_Time_Std'
]
df_out.columns = [
    'Block Size (MB)', 'Allocation_Time_Mean', 'Allocation_Time_Std', 
    'Write_Time_Mean', 'Write_Time_Std', 'Read_Time_Mean', 
    'Read_Time_Std', 'Free_Time_Mean', 'Free_Time_Std'
]

# Preparar os dados para o Box Plot
data_to_plot_in = {
    "Allocation Time": df_in['Allocation_Time_Mean'],
    "Write Time": df_in['Write_Time_Mean'],
    "Read Time": df_in['Read_Time_Mean'],
    "Free Time": df_in['Free_Time_Mean']
}

data_to_plot_out = {
    "Allocation Time": df_out['Allocation_Time_Mean'],
    "Write Time": df_out['Write_Time_Mean'],
    "Read Time": df_out['Read_Time_Mean'],
    "Free Time": df_out['Free_Time_Mean']
}

# Definir limites de y para os gráficos
limits = {
    'Allocation Time': 400,
    'Write Time': 3_000_000,
    'Read Time': 3_500_000,
    'Free Time': 1_200
}

# Função para configurar o eixo y
def format_y_axis(ax, limit):
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.ticklabel_format(useOffset=False, style='plain', axis='y')
    ax.set_ylim(0, limit)

# Criar uma figura com 4 subplots para os Box Plots de comparação
fig, axs = plt.subplots(2, 2, figsize=(14, 8))

# Gráfico para Allocation Time
axs[0, 0].boxplot([data_to_plot_in['Allocation Time'], data_to_plot_out['Allocation Time']], labels=['In Compartment', 'Out Compartment'])
axs[0, 0].set_title('Allocation Time')
axs[0, 0].set_ylabel('Time (ms)')
format_y_axis(axs[0, 0], limits['Allocation Time'])

# Gráfico para Write Time
axs[0, 1].boxplot([data_to_plot_in['Write Time'], data_to_plot_out['Write Time']], labels=['In Compartment', 'Out Compartment'])
axs[0, 1].set_title('Write Time')
axs[0, 1].set_ylabel('Time (ms)')
format_y_axis(axs[0, 1], limits['Write Time'])

# Gráfico para Read Time
axs[1, 0].boxplot([data_to_plot_in['Read Time'], data_to_plot_out['Read Time']], labels=['In Compartment', 'Out Compartment'])
axs[1, 0].set_title('Read Time')
axs[1, 0].set_ylabel('Time (ms)')
format_y_axis(axs[1, 0], limits['Read Time'])

# Gráfico para Free Time
axs[1, 1].boxplot([data_to_plot_in['Free Time'], data_to_plot_out['Free Time']], labels=['In Compartment', 'Out Compartment'])
axs[1, 1].set_title('Free Time')
axs[1, 1].set_ylabel('Time (ms)')
format_y_axis(axs[1, 1], limits['Free Time'])

# Ajustar o layout
plt.tight_layout()

# Exibir o gráfico
plt.show()

