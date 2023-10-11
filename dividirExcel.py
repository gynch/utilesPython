import pandas as pd

SPLIT_SOURCE_FILE = 'dividir.xlsx'

df = pd.read_excel(SPLIT_SOURCE_FILE,header = 0)

columns = df.columns.values.tolist()

for (centro), group in df.groupby(['CODIGOCENTRO']):
    group.to_excel(f'{centro[0]}.xlsx', index=False)
