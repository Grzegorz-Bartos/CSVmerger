import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.withdraw()

file_paths = filedialog.askopenfilenames(title="Select CSV files to merge",
                                         filetypes=[("CSV Files", "*.csv")],
                                         initialdir="/")

df_list = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    df_list.append(df)

merged_df = pd.concat(df_list, axis=1)

output_path = filedialog.asksaveasfilename(title="Save Merged CSV File As",
                                           defaultextension=".csv",
                                           filetypes=[("CSV Files", "*.csv")],
                                           initialdir="/")

merged_df.to_csv(output_path, index=False)

print(f"Merged CSV file saved at {output_path}")
