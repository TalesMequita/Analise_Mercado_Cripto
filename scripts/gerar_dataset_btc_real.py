import pandas as pd
import os

input_path = "data/btc-usd-max.csv"
output_dir = "data/"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "dados_btc_mensal_real.csv")

df = pd.read_csv(input_path)

print("Primeiras linhas do arquivo original:")
print(df.head())

df["snapped_at"] = pd.to_datetime(df["snapped_at"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

df["ano"] = df["snapped_at"].dt.year
df["mes"] = df["snapped_at"].dt.month

df_mensal = (
    df.groupby(["ano", "mes"], as_index=False)
    .agg({"price": "mean"})
    .rename(columns={"price": "preco_usd"})
)

df_mensal["data"] = pd.to_datetime(df_mensal["ano"].astype(str) + "-" + df_mensal["mes"].astype(str) + "-28")

df_mensal["moeda"] = "BTC"

df_mensal = df_mensal[["data", "moeda", "preco_usd", "ano", "mes"]]

df_mensal.to_csv(output_path, index=False)
print(f"\n Dataset mensal real do BTC salvo em: {output_path}")
print(df_mensal.head())

