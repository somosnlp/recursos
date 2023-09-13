import pandas as pd

file_name = 'datasets.csv'

original_index = 5
final_index = 4

df = pd.read_csv(file_name)

if final_index < 0 or original_index < 0 or final_index >= df.shape[1] or original_index >= df.shape[1]:
    print("Invalid column index specified.")
else:
    columns_except_original = [col for col in df.columns if col != df.columns[original_index]]

    new_columns = (
        columns_except_original[:final_index] + 
        [df.columns[original_index]] + 
        columns_except_original[final_index:]
    )

    df_reordered = df[new_columns]

    df_reordered.to_csv(file_name, index=False)

    print("Columns reordered successfully. Result saved to", file_name)
