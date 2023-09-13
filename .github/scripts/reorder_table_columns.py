import argparse
import pandas as pd

FILE_NAME = "datasets.csv"


def reorder_columns(original_index, final_index, file_name=FILE_NAME):
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

        print("Columns reordered successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reorder columns in a CSV file.")
    parser.add_argument("original_index", type=int, help="Original column index")
    parser.add_argument("final_index", type=int, help="Final column index")

    args = parser.parse_args()

    reorder_columns(args.original_index, args.final_index)
