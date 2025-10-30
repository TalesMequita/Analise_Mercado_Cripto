import pandas as pd
from sklearn.model_selection import train_test_split
import os

input_path = "data/dados_btc_mensal_real.csv"
output_path = "data/dados_btc_modelo.csv"

df = pd.read_csv(input_path)
print("Colunas Detectadas:", df.columns.tolist())

df["preco_usd"] = pd.to_numeric(df["preco_usd"], errors="coerce")
df = df.dropna(subset=["preco_usd"]) #remove linhas vazias

# Criando coluna temporal "YYYY-MM"
df["data_mensal"] = pd.to_datetime(df["ano"].astype(str) + "-" + df["mes"].astype(str) + "-01")

# Ordenando dados por tempo
df = df.sort_values("data_mensal")

# Separar apenas colunas que interessam
df_modelo = df[["data_mensal", "ano", "mes", "preco_usd"]]

# Dividir em treino e teste 80% a 20%
train, test = train_test_split(df_modelo, test_size=0.2, shuffle=False)

print(f"Tamanho treino: {len(train)} registros | teste: {len(test)} registros")

# Salvando para uso no modelo
os.makedirs("data", exist_ok=True)
df_modelo.to_csv(output_path, index=False)

print(f"\n Dataset preparado e salvo em {output_path}")
print("\n Primeiras Linhas:")
print(df_modelo.head())
