import pandas as pd
import numpy as np  
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os   

input_path = "data/dados_btc_modelo.csv"

df = pd.read_csv(input_path)
df["data_mensal"] = pd.to_datetime(df["data_mensal"])
df = df[df["ano"] >= 2020].reset_index(drop=True)
df["timestamp"] = df["data_mensal"].map(pd.Timestamp.timestamp)

x = df[["timestamp"]]
y = df[["preco_usd"]]

# Gerar polinomiais (grau 2 = cruva) serve para ler valores com muiotas curvas como valores de mercado
poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

split = int(len(df) * 0.8)
x_train, x_test = x_poly[:split], x_poly[split:]
y_train, y_test = y[:split], y[split:]

modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)  # TUDO OK

mae = mean_absolute_error(y_test, y_pred)
mse = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n Resultados do modelo de Regressão Polinominal (grau 3)")
print(f"Erro Absoluto Médio (MAE): {mae:,.2f}")
print(f"Erro Quadratico Médio (MSE): {mse:,.2f}")
print(f"Coeficiente de Determinação (R²): {r2:.4f}")

#df.loc[df.index[-len(y_test):], "preco_previsto"] = y_pred.flatten() # adicionando previsões ao DataFrame

# criando grafico real e previsto 
#plt.figure(figsize=(10,5))
#plt.plot(df["data_mensal"], df["preco_usd"], label="Preço Real", color="blue")
#plt.plot(df["data_mensal"].iloc[-len(y_test):], y_pred, label="Preço Previsto", color="orange", linestyle="--")
#plt.title("Previsão Polinominal do Preço do Bitcoin (grau 2)")
#plt.xlabel("Data")
#plt.ylabel("Preço (USD)")
#plt.legend()
#plt.grid(True)

df["media_movel"] = df["preco_usd"].rolling(window=3).mean() # MEDIA MOVEL 3 MESES

plt.plot(df["data_mensal"], df["preco_usd"], label="Preço Real", color="blue", linewidth=1.8) #LINHA REAL
plt.plot(df["data_mensal"], df["media_movel"], label="Média Movel (3 meses)", color="green", linestyle="--", linewidth=1.8) # LINHA MEDIA MOVEL
plt.plot(df["data_mensal"].iloc[-len(y_test):], y_pred, label="Preço Previsto", color="orange", linestyle="--", linewidth=2) # LINHA PREVISAO

plt.title("Previsão Polinominal do Preço do Bitcoin (grau 3) com Media Movel")
plt.xlabel("Data")
plt.ylabel("Preço (USD)")
plt.legend()
plt.grid(True)

os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/previsao_polinominal_btc.png", dpi=300)
plt.show()

print("\n Gráfico salvo em: outputs/previsao_linear_btc.png")

# Gerar Previsoes futuras 3 meses a frente
ultimo_timestamp = df["timestamp"].iloc[-1]
futuros = np.array([ultimo_timestamp + i * 2629746 for i in range(1, 4)]).reshape(-1, 1) # 1 mes = 2629746 segundos
futuros_poly = poly.transform(futuros)
previsoes_futuras = modelo.predict(futuros_poly)

print("\n Previsões para os proximos 3 meses:")
for i, valor in enumerate(previsoes_futuras, start=1):
    print(f"Mês +{i}: {float(valor):,.2f} USD")