import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import ScalarFormatter

# Load the two CSV files, treating periods as thousand separators
try:
    df_in = pd.read_csv('../summarise-results/aggregated-memory-in-results.csv', thousands='.')
    df_out = pd.read_csv('../summarise-results/aggregated-memory-out-results.csv', thousands='.')
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

# Print the column names to ensure they match expectations
print("Columns in aggregated-memory-in-results.csv:", df_in.columns)
print("Columns in aggregated-memory-out-results.csv:", df_out.columns)

# Keep only the columns relevant to the means
expected_columns = ['Block Size (MB)', 'Allocation_Time_Mean', 'Write_Time_Mean', 'Read_Time_Mean', 'Free_Time_Mean']
if not set(expected_columns).issubset(df_in.columns) or not set(expected_columns).issubset(df_out.columns):
    print("Error: Expected columns for mean values are not present in one or both files.")
    exit()

# Select only the required columns for plotting
df_in = df_in[expected_columns]
df_out = df_out[expected_columns]

# Set column names for clarity
df_in.columns = ['Block Size (MB)', 'Allocation Time (ms)', 'Write Time (ms)', 'Read Time (ms)', 'Free Time (ms)']
df_out.columns = ['Block Size (MB)', 'Allocation Time (ms)', 'Write Time (ms)', 'Read Time (ms)', 'Free Time (ms)']

# Group by block size (optional, data is already grouped) and calculate the mean for each operation
df_in_means = df_in.set_index('Block Size (MB)')
df_out_means = df_out.set_index('Block Size (MB)')

# Create a figure with 4 subplots (2x2) organized for each time type
fig, axs = plt.subplots(2, 2, figsize=(14, 8))

# Plot Allocation Time
axs[0, 0].plot(df_in_means.index, df_in_means['Allocation Time (ms)'], label='In Compartment', marker='o')
axs[0, 0].plot(df_out_means.index, df_out_means['Allocation Time (ms)'], label='Out Compartment', marker='o')
axs[0, 0].set_title('Allocation Time')
axs[0, 0].set_xlabel('Block Size (MB)')
axs[0, 0].set_ylabel('Time (ms)')
axs[0, 0].legend()

# Plot Write Time
axs[0, 1].plot(df_in_means.index, df_in_means['Write Time (ms)'], label='In Compartment', marker='o')
axs[0, 1].plot(df_out_means.index, df_out_means['Write Time (ms)'], label='Out Compartment', marker='o')
axs[0, 1].set_title('Write Time')
axs[0, 1].set_xlabel('Block Size (MB)')
axs[0, 1].set_ylabel('Time (ms)')
axs[0, 1].yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
axs[0, 1].ticklabel_format(style='plain', axis='y')
axs[0, 1].legend(loc='best')

# Plot Read Time
axs[1, 0].plot(df_in_means.index, df_in_means['Read Time (ms)'], label='In Compartment', marker='o')
axs[1, 0].plot(df_out_means.index, df_out_means['Read Time (ms)'], label='Out Compartment', marker='o')
axs[1, 0].set_title('Read Time')
axs[1, 0].set_xlabel('Block Size (MB)')
axs[1, 0].set_ylabel('Time (ms)')
axs[1, 0].yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
axs[1, 0].ticklabel_format(style='plain', axis='y')
axs[1, 0].legend(loc='best')

# Plot Free Time
axs[1, 1].plot(df_in_means.index, df_in_means['Free Time (ms)'], label='In Compartment', marker='o')
axs[1, 1].plot(df_out_means.index, df_out_means['Free Time (ms)'], label='Out Compartment', marker='o')
axs[1, 1].set_title('Free Time')
axs[1, 1].set_xlabel('Block Size (MB)')
axs[1, 1].set_ylabel('Time (ms)')
axs[1, 1].legend(loc='best')

# Adjust layout for better readability
plt.tight_layout()

# Display the plot
plt.show()

