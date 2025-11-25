# 🚀 Projeto — Análise Mercado Criptomoedas

## 👥 Integrantes
- **Matheus Dias da Silva** — RA:2222200299
- **Tales Mequita Fernandes** — RA:2222201254

Turma:41|Curso:Ciência da computação|Período: Noturno|Ano: 2025

## Problema
A oscilação do preço do Bitcoin torna difícil para iniciantes compreenderem sua tendência e comportamento histórico. Sem modelos acessíveis de análise e previsão, muitos usuários tomam decisões sem base técnica ou dados reais.

## Abordagem de IA
O projeto utiliza Regressão Polinomial de Grau 2, combinada com padronização dos dados (StandardScaler) e suavização por Média Móvel, para gerar previsões mais estáveis do preço do Bitcoin.
Essa abordagem é adequada porque captura variações não lineares e torna as previsões menos sensíveis a flutuações abruptas, comuns no mercado de criptomoedas.

A métrica principal utilizada é o *MAE (Erro Absoluto Médio)*, por ser mais interpretável em cenários financeiros.

## Dados
Os dados foram obtidos manualmente nas plataformas públicas *CoinGecko* e *CoinMarketCap*, que fornecem histórico oficial de preços do Bitcoin.Os arquivos CSV foram tratados, limpos e convertidos em uma base mensal utilizada no modelo de previsão.

## Como reproduzir

## ativar ambiente
pip install -r requirements.txt
python src/main.py --seed 42

## Resultados do Projeto
MAE, MSE e R² calculados durante os testes do modelo.
Geração automática de gráfico futuro: outputs/previsao_futura_IA.png.
Interpretação automática indicando tendência (Alta, Queda ou Estabilidade).

## Gráficos principais (gerados pelo app):
Histórico de preços
Média móvel
Previsão contínua para os próximos meses

## 🛠️ Tecnologias Utilizadas
- Python 🐍  
- GitHub 💻  

## 📦 Bibliotecas Utilizadas
- pandas -- leitura, limpeza e manipulação de dados
- numpy -- operações matemáticas e vetorização
- scikit-learn -- modelo IA (regressão polinominal)
- matplotlib -- gerador de gráficos
- streamlit -- criação da interface web
- python-dateutil / pandas.DateOffset -- projeção de datas futuras
- os -- manipulação de diretórios e caminhos
- datetime -- manipulção pontual de datas

## 🚀 Como Utilizar o Projeto — Passo a Passo Completo
