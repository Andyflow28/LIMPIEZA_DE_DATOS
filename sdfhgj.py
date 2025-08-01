import pandas as pd

# Cargar datos
df = pd.read_csv("dirty_cafe_sales.csv")

# Vista general
print(df.head())
print(df.info())
print(df.isnull().sum())  # Valores nulos
print(df.duplicated().sum())  # Filas duplicadas