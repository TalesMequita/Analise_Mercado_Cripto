import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

input_path = "outputs/estatisticas_btc_mensal.csv"
output_dir = "outputs/"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(input_path, sep=";")

cols_numericas = ["media_preco", "preco_min", "preco_max", "variacao_percentual"]
df[cols_numericas] = df[cols_numericas].apply(pd.to_numeric, errors="coerce")

print("Colunas numéricas convertidads com suceeso!\n")
print(df[cols_numericas].head())

corr = df[cols_numericas].corr()
print("\n Matriz da correlação: \n", corr)

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlção - Variveis do BTC (Mensal)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "matriz_correlacao_btc.png"), dpi=300)
plt.close()

print("\n Heatmap salvo em: output/matriz_correlacao_btc.png")
