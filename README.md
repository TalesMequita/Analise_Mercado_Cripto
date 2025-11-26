# 🚀 Projeto — Análise Mercado Criptomoedas

## 👥 Integrantes
- **Matheus Dias da Silva** — RA:2222200299
- **Tales Mequita Fernandes** — RA:2222201254

Turma:41|Curso:Ciência da computação|Período: Noturno|Ano: 2025

## 🧩 Problema
A oscilação do preço do Bitcoin torna difícil para iniciantes compreenderem sua tendência e comportamento histórico. Sem modelos acessíveis de análise e previsão, muitos usuários tomam decisões sem base técnica ou dados reais.

## 🤖 IA / Técnica Utilizada

O projeto utiliza:
- Regressão Polinomial (Grau 2)

Modelo que captura variações não lineares do preço, ideal para dados financeiros.

- StandardScaler

Padroniza os dados antes do treino, melhorando o desempenho.

- Média Móvel (3 meses)

Suaviza oscilações para reduzir ruído e melhorar a interpretação.

- Por que esta abordagem é adequada?

O Bitcoin possui movimentos curvos e ciclos → regressão polinomial captura esses padrões.

O mercado tem muitos picos e quedas → média móvel ameniza ruídos.

Previsões financeiras exigem estabilidade → combinação das técnicas reduz exageros estatísticos.

## 📊 Dados
Os dados foram obtidos manualmente nas plataformas públicas *CoinGecko* e *CoinMarketCap*, que fornecem histórico oficial de preços do Bitcoin.Os arquivos CSV foram tratados, limpos e convertidos em uma base mensal *(dados_btc_mensal_real.csv)* utilizada no modelo de previsão.

## 🔁 Como o Projeto Funciona (Fluxo Interno)

- O usuário clica em Rodar Previsão IA na interface.
- O app carrega o dataset mensal do Bitcoin.
- Os dados são padronizados com StandardScaler.
- O modelo aplica Regressão Polinomial de Grau 2.
- A previsão é suavizada e exibida graficamente.

#### O sistema calcula automaticamente:
- Maior alta do ano
- Pior baixa
- Preço atual
- Interpretação da tendência (alta, queda ou estável)

## 📈 Resultados Gerados
MAE, MSE e R² calculados durante os testes do modelo.
Geração automática de gráfico futuro: outputs/previsao_futura_IA.png.
Interpretação automática indicando tendência (Alta, Queda ou Estabilidade).

## 🛠️ Tecnologias Utilizadas
- Python 3.11   
- GitHub 
- pandas
- numpy
- matplotlib
- scikit-learn
- streamlit (interface web)

## 📦 Bibliotecas Utilizadas
- pandas
- numpy
- scikit-learn
- matplotlib
- streamlit
- python-dateutil (DateOffset)
- os
- datetime
#### *todas estão no arquivo requiremnets.txt, nãop é necessario nenhuma outra biblioteca*

## 📂 Estrutura de Pastas do Projeto
![alt text](image.png)

## 🚀 Como Utilizar o Projeto — Passo a Passo Completo
#### No terminal do vsCode crie o ambiente virtual (Python 3.11)
- py -3.11 -m venv venv
#### Instalar depenências
- py -3.11 -m pip install -r requirements.txt
#### Instalar streamlit 
- py -3.11 -m pip install streamlit
#### Executar o dashboard 
- py -3.11 -m streamlit run app/app.py

#### 🔁 Observação importante
Antes de rodar qualquer comando, entre na pasta principal do projeto:

- cd Analise_Mercado

Depois disso, siga os passos normalmente:

ativar o ambiente virtual

instalar as dependências

rodar o Streamlit

Assim, a página web será aberta automaticamente no navegador.
