import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

sns.set_theme(style="whitegrid", palette="muted") #colocando estilo

input_path = "outputs/estatisticas_btc_mensal.csv" #caminho para buscar as estatisticas
output_dir = "outputs/"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(input_path, sep=";") # indicando para seprar na ;

print("Colunas detectadas", df.columns.tolist())
print("\nPrimeiras Linhas:\n", df.head())

df = df.sort_values(by=["ano", "mes"])   # garantindo que os meses erstão certos

# Grafico 1 abaixo
plt.figure(figsize=(12, 6))
sns.lineplot(x="mes", y="media_preco", hue="ano", data=df, marker="o")
plt.title("Tendência Mensal do Preço Médio do BTC (poor ano)")
plt.xlabel("Mês")
plt.ylabel("Preço Médio (USD)")
plt.legend(title="ano")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_tendencia_btc.png"), dpi=300)
plt.close()

print("Gráfico 1 salvo: grafico_tendencia_btc.png")

# Grafico 2 abaixo
plt.figure(figsize=(12, 6))
sns.barplot(x="mes", y="variacao_percentual", hue="ano", data=df)
plt.axhline(0, color="gray", linestyle="--", linewidth=1)
plt.title("Variação Percentual Mensal do BTC (por ano)")
plt.xlabel("Mês")
plt.ylabel("Variação (%)")
plt.legend(title="ano")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_variacao_btc.png"), dpi=300)
plt.close()

print("Gráfico 2 salvo: grafico_variacao_btc.png")

print("\n Gráficos gerados e salvos na pasta 'outputs/' com sucesso!")

