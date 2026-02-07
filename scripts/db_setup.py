import sqlite3
import pandas as pd
from pathlib import Path

# Paths
DB_PATH = Path("data/esports.db")
CSV_PATH = Path("data/matches.csv")

# Load CSV
df = pd.read_csv(CSV_PATH)

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)

# Write to database
df.to_sql("matches", conn, if_exists="replace", index=False)

conn.close()

print("Database created and populated successfully ✅")
