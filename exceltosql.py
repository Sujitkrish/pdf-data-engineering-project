import pandas as pd
from sqlalchemy import create_engine

server = "localhost"
database = "databasename"

engine = create_engine(
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Read Excel
df = pd.read_excel("output.xlsx")

# Create/replace table
df.to_sql(
    "TableName",
    con=engine,
    if_exists="replace",  # replace, append, fail
    index=False
)

print("Data loaded successfully.")
