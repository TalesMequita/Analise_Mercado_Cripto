import pandas as pd
import numpy as np
import os

input_path = "data/dados_btc_mensal_real.csv"

df = pd.read_csv(input_path)
df["preco_usd"] = df["preco_usd"].astype(str).str.replace(",",".").astype(float) # ajusta o separador da planilha , para .

print("Colunas detectadas:", list(df.columns))
print("\nPrimeiras linhas:")
print(df.head())

df["data"] = pd.to_datetime(df["data"], dayfirst=True)

media = df["preco_usd"].mean()
desvio = df["preco_usd"].std()
maximo = df["preco_usd"].max()
minimo = df["preco_usd"].min()

print("\n Estatisticas básicas gerais:")
print(f"Média geral: {media:,.2f} USD")
print(f"Desvio padrão: {desvio:,.2f} USD")
print(f"Maior preço: {maximo:,.2f} USD")
print(f"Menor preço: {minimo:,.2f} USD")

estatisticas = df.groupby(["ano", "mes"]).agg(
    media_preco=("preco_usd", "mean"),
    desvio_padrao=("preco_usd", "std"),
    preco_min=("preco_usd", "min"),
    preco_max=("preco_usd", "max")
).reset_index()

# Calcula cariação percentual entre trimestre consecutivos
estatisticas["variacao_percentual"] = estatisticas["media_preco"].pct_change() * 100

print("\nEstatítsticas por trimestre:")
print(estatisticas)

os.makedirs("outputs", exist_ok=True) #conferindo se a pasta outpus existe

estatisticas.to_csv("outputs/estatisticas_btc_mensal.csv", index=False, sep=";") #salvando o resultado

print("\n Estatísticas salvas em: outputs/estatisticas_btc_mensal.csv")
