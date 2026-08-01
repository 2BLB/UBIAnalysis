import sqlite3
import pandas as pd

# Connect to new database
conn = sqlite3.connect("crimedatacsv_new.db")

# Load CSV files
la_crime = pd.read_csv("la_crime_1500.csv")
local_crime = pd.read_csv("local_crime_1500.csv")
cps_income = pd.read_csv("cps_income_1500.csv")

# Write tables
la_crime.to_sql(
    "la_crime",
    conn,
    index=False,
    if_exists="replace"
)

local_crime.to_sql(
    "local_crime",
    conn,
    index=False,
    if_exists="replace"
)

cps_income.to_sql(
    "cps_income",
    conn,
    index=False,
    if_exists="replace"
)

conn.close()

print("Database created successfully!")