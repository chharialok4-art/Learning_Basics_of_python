import pandas as pd
from pathlib import Path
BASE_PATH=Path(__file__).resolve().parent
file_path=BASE_PATH/"sample_file.csv"
directory=pd.read_csv(file_path)
print(directory)