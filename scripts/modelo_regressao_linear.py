import pandas as pd
import numpy as np  
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os   

def rodar_previsao():
    input_path = "data/dados_btc_modelo.csv"

    df = pd.read_csv(input_path)
    df["data_mensal"] = pd.to_datetime(df["data_mensal"])
    df = df[df["ano"] >= 2020].reset_index(drop=True)

    # Criar índice simples (mes_num) em vez de timestamp
    df["mes_num"] = np.arange(len(df))
    x = df[["mes_num"]]
    y = df[["preco_usd"]]

    scaler_x = StandardScaler()
    scaler_y = StandardScaler()
    x_scaled = scaler_x.fit_transform(x)
    y_scaled = scaler_y.fit_transform(y)


    # Gerar polinomiais (grau 2 = cruva) 
    poly = PolynomialFeatures(degree=2)
    x_poly = poly.fit_transform(x_scaled)

    split = int(len(df) * 0.8)
    x_train, x_test = x_poly[:split], x_poly[split:]
    y_train, y_test = y_scaled[:split], y_scaled[split:]

    modelo = LinearRegression()
    modelo.fit(x_train, y_train)

    # PREVISÕES
    y_pred_scaled = modelo.predict(x_test)
    y_pred = scaler_y.inverse_transform(y_pred_scaled)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n Resultados do modelo de Regressão Polinominal (grau 2)")
    print(f"Erro Absoluto Médio (MAE): {mae:,.2f}")
    print(f"Erro Quadratico Médio (MSE): {mse:,.2f}")
    print(f"Coeficiente de Determinação (R²): {r2:.4f}")
    
    df["media_movel"] = df["preco_usd"].rolling(window=3).mean() # MEDIA MOVEL 3 MESES

    plt.figure(figsize=(10,5))
    plt.plot(df["data_mensal"], df["preco_usd"], label="Preço Real", color="blue", linewidth=1.8) #LINHA REAL
    plt.plot(df["data_mensal"], df["media_movel"], label="Média Movel (3 meses)", color="green", linestyle="--", linewidth=1.8) # LINHA MEDIA MOVEL
    #plt.plot(df["data_mensal"].iloc[-len(y_test):], y_pred, label="Preço Previsto", color="orange", linestyle="--", linewidth=2) # LINHA PREVISAO

    # --- Linha de previsão contínua (em sequência ao gráfico real) ---
    ultima_data_real = df["data_mensal"].iloc[-1]
    ultima_data_valor = df["preco_usd"].iloc[-1]

    # Gera 3 novas datas mensais à frente (simulando os meses futuros)
    datas_prev = [ultima_data_real + pd.DateOffset(months=i) for i in range(1, 4)]

    # Liga o último ponto real ao início da previsão (linha contínua)
    plt.plot(
        [ultima_data_real] + datas_prev,
        [ultima_data_valor] + y_pred[:3].flatten().tolist(),
        label="Preço Previsto (grau 2)",
        color="orange",
        linestyle="--",
        linewidth=2
    )

    plt.title("Previsão Polinominal do Preço do Bitcoin (grau 2) com Media Movel")
    plt.xlabel("Data")
    plt.ylabel("Preço (USD)")
    plt.legend()
    plt.grid(True)

    os.makedirs("outputs", exist_ok=True)
    grafico_path = "outputs/previsao_futura_IA.png"
    plt.savefig(grafico_path, dpi=300)
    plt.close()

    print("\n Gráfico salvo em: {grafico_path}")

    # ANALISE RESUMIDA DO ANO
    ano_atual = df["data_mensal"].max().year
    df_ano = df[df["data_mensal"].dt.year == ano_atual]

    if not df_ano.empty:
        preco_max = df_ano["preco_usd"].max()
        data_max = df_ano.loc[df_ano["preco_usd"].idxmax(), "data_mensal"].strftime("%d/%m/%Y")

        preco_min = df_ano["preco_usd"].min()
        data_min = df_ano.loc[df_ano["preco_usd"].idxmin(), "data_mensal"].strftime("%d/%m/%Y")

        preco_atual = df_ano.iloc[-1]["preco_usd"]
        data_atual = df_ano.iloc[-1]["data_mensal"].strftime("%d/%m/%Y")
    else:
        preco_max = preco_min = preco_atual = np.nan
        data_max = data_min = data_atual = "—"

    resumo_df = pd.DataFrame({
        "Indicador": ["📈 Maior Alta", "💵 Preço Atual", "📉 Pior Baixa"],
        "Valor (USD)": [preco_max, preco_atual, preco_min],
        "Data": [data_max, data_atual, data_min]
    })

    # INTERPRETAÇÃO AUTOMATICA
    tendencia = y_pred[-1] - y_pred[0]
    if tendencia > 0:
        interpretacao = "📈 Tendência de alta nos próximos meses."
    elif tendencia < 0:
        interpretacao = "📉 Tendência de queda nos próximos meses."
    else:
        interpretacao = "🔸 Mercado estável nos próximos meses."

    return resumo_df, interpretacao, grafico_path