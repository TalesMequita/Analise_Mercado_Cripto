import pandas as pd
import os

estatisticas_path = "outputs/estatisticas_btc_mensal.csv"
correlacao_img = "outputs/matriz_correlacao_btc.png"
grafico_tendencia = "outputs/grafico_tendencia_btc.png"
grafico_variacao = "outputs/grafico_variacao_btc.png"
relatorio_path = "outputs/relatorio_2.md"

df = pd.read_csv(estatisticas_path, sep=";")
media_geral = df["media_preco"].mean()
desvio_geral = df["media_preco"].std()
preco_max = df["preco_max"].max()
preco_min = df["preco_min"].min()

with open(relatorio_path, "w", encoding="utf-8") as f:
    f.write("----- RELATÓRIO 2 - ANALISE MENSAL BTC -----\n\n")
    f.write("Estatísticas Gerais:\n")
    f.write(f"Média Geral: {media_geral:,.2f} USD\n")
    f.write(f"Desvio Padrão: {desvio_geral:,.2f} USD\n")
    f.write(f"Maior Preço: {preco_max:,.2f} USD\n")
    f.write(f"Menor Preço: {preco_min:,.2f} USD\n\n")

    f.write("Arquivos gerados\n")
    f.write(f" - Gráfico de Tendência: {grafico_tendencia}\n")
    f.write(f" - Gráfico de Variação: {grafico_variacao}\n")
    f.write(f" - Matriz de Correlação: {correlacao_img}\n")
    f.write(f" - Base Consolidada: {estatisticas_path}\n\n")

    f.write("Interpretação Geral:\n")
    f.write("TEXTO TESTE\n\n")

    f.write("Etapa 2 concluida com Sucesso!")

print(f"Relatorio final salvo em: {relatorio_path}")