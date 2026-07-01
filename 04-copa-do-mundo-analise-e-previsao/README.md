# ⚽ Copa do Mundo: Fator Casa, Evolução do Jogo e Previsão de Público

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualiza%C3%A7%C3%A3o-11557C?logo=plotly&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Regress%C3%A3o%20Linear-F7931E?logo=scikitlearn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-Testes%20Estat%C3%ADsticos-8CAAE6?logo=scipy&logoColor=white)

## 📌 Sobre o projeto

Análise de dados históricos da Copa do Mundo (1930–2014) para investigar duas crenças populares sobre o torneio e, em seguida, construção de um modelo preditivo para estimar a média de público de edições futuras — validado contra os resultados reais de 2018 e 2022.

O projeto é dividido em duas etapas complementares:

1. **Análise Exploratória** — testar hipóteses com estatística descritiva e correlação de Pearson.
2. **Modelagem Preditiva** — regressão linear para previsão de público, com avaliação honesta das limitações do modelo.

## ❓ Perguntas de pesquisa

| # | Pergunta | Método |
|---|----------|--------|
| 1 | O país-sede tem vantagem por jogar em casa? | Comparação de taxa de vitória, média de gols e fase alcançada (casa vs. fora) |
| 2 | A competição ficou mais equilibrada ao longo do tempo? | Média de gols por edição, correlação de Pearson (ano x média de gols) |
| 3 | É possível prever a média de público de copas futuras a partir da tendência histórica? | Regressão linear (ano → público médio por partida), validada contra dados reais de 2018/2022 |

## 🔍 Principais resultados

**Fator casa:** o país-sede vence a maioria das partidas e, em 12 das 16 edições analisadas, fez mais gols em casa do que como visitante. Porém, a vantagem é mais decisiva para seleções sem tradição no futebol (ex: Suécia em 1958, Coreia do Sul em 2002) — para potências tradicionais (Brasil, Alemanha, Itália), jogar em casa não altera significativamente o desempenho.

**Evolução da competitividade:** a média de gols por partida caiu de forma estatisticamente significativa ao longo do tempo (correlação de Pearson, valor-p < 0,05), com estabilização a partir da década de 1980 — consistente com a hipótese de que o nível técnico das seleções se tornou mais parelho.

**Previsão de público:** o modelo de regressão linear simples (ano → público médio) obteve R² próximo de 0,5, o que indica que a tendência temporal explica apenas parte da variação. Isso é esperado e discutido no notebook: fatores como capacidade dos estádios e número de seleções participantes, não incluídos no modelo, também influenciam fortemente o público — um bom exercício de regressão, mas com humildade estatística sobre suas limitações.

## 🛠️ Metodologia

- **Preparação dos dados:** tratamento de país-sede duplicado (Copa de 2002, Japão/Coreia do Sul), padronização de nomenclatura de fases entre diferentes edições, tradução de nomes de países via `deep-translator`.
- **Análise exploratória:** agregações com `pandas` (`groupby`, `merge`), visualizações comparativas com `matplotlib` (gráficos de pizza, barras e dispersão).
- **Teste de hipótese:** correlação de Pearson (`scipy.stats.pearsonr`) para validar a tendência de queda na média de gols.
- **Modelagem:** `LinearRegression` do `scikit-learn`, com avaliação via R² e RMSE (`sklearn.metrics`), e validação out-of-sample comparando previsões com valores reais observados.

## 📂 Fonte dos dados

Datasets públicos do Kaggle: [WorldCupMatches.csv](.) e [WorldCups.csv](.), com resultados de todas as partidas e resumos de todas as edições da Copa do Mundo de 1930 a 2014.

## ▶️ Como executar

```bash
pip install pandas matplotlib scikit-learn scipy deep-translator
jupyter notebook notebooks/01_analise_exploratoria.ipynb
jupyter notebook notebooks/02_regressao_media_publico.ipynb
```

## 🚧 Limitações e próximos passos

- O modelo de regressão usa apenas o ano como variável preditora; incluir número de seleções e capacidade média dos estádios provavelmente melhoraria o R².
- Poderia ser estendido com modelos não-lineares ou validação cruzada para reforçar a robustez estatística.
