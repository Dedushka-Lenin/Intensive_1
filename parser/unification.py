import pandas as pd    #  pip install pandas
import glob
from pathlib import Path

data_dir = Path("base")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

combined_csv.to_csv( "./res.csv", index=False, encoding='utf-8-sig')