import pandas as pd

for archivo in ['nodos.xlsx', 'proyecto.xlsx']:
    df = pd.read_excel(archivo)
    print(f"--- {archivo} ---")
    print(df.columns)
    print(df.head())
    print()