import camelot
import pandas as pd

tables = camelot.read_pdf("Datasync.pdf", pages="all")

with pd.ExcelWriter("output.xlsx") as writer:
    for i, table in enumerate(tables):

        df = table.df
        df.columns = df.iloc[0]   # Use first row as header
        df = df[1:]  # Remove header row from data
        df.reset_index(drop=True, inplace=True)  # Reset index
        df.to_excel(
            writer,
            sheet_name=f"Table_{i+1}",
            index=False
        )

print("Excel file created successfully.")