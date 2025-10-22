import pandas as pd

caminho_csv = "data/dados_cripto_teste.csv"

try:
    df = pd.read_csv(caminho_csv, sep=";")
    print("CSV lido com sucesso!\n")
    print("Primeiras linhas do arquivo:")
    print(df.info(), "\n")

    print("Informações Gerais:")
    print(df.info(), "\n")

    print("Colunas Detectadas:", list(df.columns))
except FileExistsError:
    print("Arquivo CSV não encontrado. Verifique o caminh do arquivo")
except Exception as e:
    print("Erro ao ler o CSV:", e)