import pandas as pd
from pathlib import Path

root_path = Path(__file__).resolve().parent
data_path = root_path / "data"
xlsx_path = data_path / "uncleaned_data.xlsx"
csv_path = data_path / "uncleaned_data.csv"

df = pd.read_excel(xlsx_path)

df.to_csv(csv_path, index=False, encoding="utf-8")