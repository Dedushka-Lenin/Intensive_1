import pandas as pd
from pathlib import Path

data_dir = Path("parser/base")  # Папка с csv

df = pd.concat([pd.read_csv(f) for f in data_dir.glob("*.csv")], ignore_index=True)
df.to_csv("parser/result.csv", index=False) # Файл с результатом