import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.title("CSV Merger")

# window dimensions
width = 400
height = 300

# screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# coordinates
x = (screen_width - width) // 2
y = (screen_height - height) // 2

# setting the position of the window
root.geometry(f"{width}x{height}+{x}+{y}")
file_paths = ""


def choose():
    global file_paths
    file_paths = filedialog.askopenfilenames(title="Select CSV files to merge",
                                             filetypes=[("CSV Files", "*.csv")],
                                             initialdir="/")
    if file_paths != "":
        button.config(text="save", command=save)
    else:
        root.quit()


def save():
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

    button.config(text="save", command=choose)

    label.config(text=f"Merged CSV file saved at {output_path}")


label = tk.Label(root, text="Merge CSV files")
label.pack(pady=50)
button = tk.Button(root, text="Select", command=choose)
button.pack()

root.mainloop()
