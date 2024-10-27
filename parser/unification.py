import pandas as pd    #  pip install pandas
from pathlib import Path

def csv_merger(path, out_filename="res.csv", globmask="*.csv", chunksize=5000, **kwargs):
    path = Path(path)
    need_header = True
    for f in path.glob(globmask):
        for chunk in pd.read_csv(f, chunksize=chunksize, **kwargs):
            chunk.to_csv(out_filename, index=False, header=need_header, mode="a")
            need_header = False

csv_merger("/parser/base", "parser/base/res.csv", globmask="*.csv", chunksize=1000)