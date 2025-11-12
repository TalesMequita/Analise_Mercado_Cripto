import sys
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from scripts.modelo_regressao_linear import rodar_previsao

st.set_page_config(
    page_title="Analise de Mercado - Cripto AI",
    page_icon="💰",
    layout="centered"
)

st.title("Análise de Mercado com Inteligência Artificial")
st.subheader("Previsão e análise de tendências de Criptomoedas")
st.write("Selecione a moeda e o período para visualizar a variação dos preços.")

st.divider()
data_path = Path("data/dados_btc_mensal_real.csv")

if data_path.exists():
    df = pd.read_csv(data_path)
    st.success("✅ Dataset carregado com sucesso!")
else:
    st.error("❌ Arquivo não encontrado.")
    st.stop()

df["data"] = pd.to_datetime(df["data"])

moeda = st.selectbox("Selecione a moeda para análise:", ["BTC"])

opcoes_periodo = [
    "Últimos 3 meses",
    "Últimos 6 meses",
    "Últimos 12 meses",
    "Todo o histórico"
]
periodo = st.selectbox("Selecione o período de análise:", opcoes_periodo)

hoje = df["data"].max()
if periodo == "Últimos 3 meses":
    data_inicio = hoje - pd.DateOffset(months=3)
elif periodo == "Últimos 6 meses":
    data_inicio = hoje - pd.DateOffset(months=6)
elif periodo == "Últimos 12 meses":
    data_inicio = hoje - pd.DateOffset(months=12)
else:
    data_inicio = df["data"].min()

df_filtrado = df[df["data"] >= data_inicio]

st.subheader(f"📊 Evolução do preço - {moeda}")
st.write(f"Período exibido: **{data_inicio.strftime('%d/%m/%Y')}** até **{hoje.strftime('%d/%m/%y')}**")

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(df_filtrado["data"], df_filtrado["preco_usd"], marker='o', linestyle="-", linewidth=2)
ax.set_xlabel("Data")
ax.set_ylabel("Preço (USD)")
ax.set_title("Tendência de preço do {moeda}")
ax.grid(True)
st.pyplot(fig)

variacao = ((df_filtrado["preco_usd"].iloc[-1] / df_filtrado["preco_usd"].iloc[0]) -1) * 100
tendencia = "alta 📈" if variacao > 0 else "queda 📉"

st.subheader ("Relatório Automático")
st.write(f"No período selecionado, o **Bitcoin** apresentou uma variação de **{variacao:.2f}%**, indicando uma tendência de **{tendencia}**.")

if st.button("🚀 Rodar previsão IA"):
    resumo_df, interpretacao, grafico_path = rodar_previsao()
    st.image(grafico_path)
    st.dataframe(resumo_df)
    st.markdown(f"### {interpretacao}")