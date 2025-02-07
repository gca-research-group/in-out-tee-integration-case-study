import pandas as pd

# Load the data from the CSV file
file_path = "../outside-tee-exection/memory-out-experiment-result.csv"
data = pd.read_csv(file_path)

# Convert numeric columns, remove thousand separators, and force to float
numeric_columns = ["Allocation Time (ms)", "Write Time (ms)", "Read Time (ms)", "Free Time (ms)"]
for column in numeric_columns:
    data[column] = data[column].replace(r'\.', '', regex=True).astype(float)

# Group the data by block size and calculate the mean and standard deviation for each group
result = data.groupby("Block Size (MB)").agg(
    Allocation_Time_Mean=('Allocation Time (ms)', 'mean'),
    Allocation_Time_Std=('Allocation Time (ms)', 'std'),
    Write_Time_Mean=('Write Time (ms)', 'mean'),
    Write_Time_Std=('Write Time (ms)', 'std'),
    Read_Time_Mean=('Read Time (ms)', 'mean'),
    Read_Time_Std=('Read Time (ms)', 'std'),
    Free_Time_Mean=('Free Time (ms)', 'mean'),
    Free_Time_Std=('Free Time (ms)', 'std')
).reset_index()

# Round and format the values
result['Allocation_Time_Mean'] = result['Allocation_Time_Mean'].round(0).astype(int)
result['Allocation_Time_Std'] = result['Allocation_Time_Std'].round(2)
result['Write_Time_Mean'] = result['Write_Time_Mean'].round(0).apply(lambda x: f"{int(x):,}".replace(",", "."))
result['Write_Time_Std'] = result['Write_Time_Std'].round(2)
result['Read_Time_Mean'] = result['Read_Time_Mean'].round(0).apply(lambda x: f"{int(x):,}".replace(",", "."))
result['Read_Time_Std'] = result['Read_Time_Std'].round(2)
result['Free_Time_Mean'] = result['Free_Time_Mean'].round(0).astype(int)
result['Free_Time_Std'] = result['Free_Time_Std'].round(2)

# Filter to ensure we are only taking block sizes between 100 and 1000 (1 to 10 times 100)
result = result[result["Block Size (MB)"].isin([i * 100 for i in range(1, 11)])]

# Save the result to a new CSV file
output_file_path = "aggregated-memory-out-results.csv"
result.to_csv(output_file_path, index=False)

print("Results saved to:", output_file_path)
print(result)

