import pandas as pd    #  pip install pandas
from pathlib import Path

data_dir = Path("parser/base")

df = pd.concat([pd.read_csv(f) for f in data_dir.glob("*.csv")], ignore_index=True)
df.to_csv("parser/result.csv", index=False)