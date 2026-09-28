import pandas as pd
from pathlib import Path

# Get the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent

# Create the path to creditcard.csv
csv_path = BASE_DIR / "creditcard.csv"

# Load CSV
df = pd.read_csv(csv_path)

print(df.to_numpy);
