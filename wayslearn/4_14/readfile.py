import numpy as np
import pandas as pd

sheet1=pd.read_excel("score.xls",sheet_name="第一组红葡萄酒品尝评分",header=None)

class ScoreTable:
    def __init__(self, data):
        self.data = data

indexs = []
tables = []
for i in range(2, 367, 14):
    n = int(sheet1.iloc[i, 0][3:])
    indexs.append(n)
    # Extract 14 rows for each table
    table_data = sheet1.iloc[i:i+14].reset_index(drop=True)
    tables.append(ScoreTable(table_data))

print(indexs)
print(f"Extracted {len(tables)} tables")

# Display each table
for idx, table in enumerate(tables):
    print(f"\nTable {indexs[idx]}:")
    print(table.data)