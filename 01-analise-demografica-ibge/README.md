# 📊 Envelhecimento Populacional Brasileiro — Análise com Dados do IBGE

Análise exploratória da evolução da pirâmide etária brasileira entre 2000 e 2022, com base nos dados dos Censos Demográficos do IBGE. O projeto investiga o processo de envelhecimento da população, identifica os estados mais vulneráveis à inversão etária e discute suas implicações socioeconômicas.

---

## 🔍 Perguntas que o projeto responde

- Como a pirâmide etária brasileira mudou entre 2000, 2010 e 2022?
- Quais regiões do Brasil têm maior concentração de jovens? E de idosos?
- Quais estados apresentam maior desequilíbrio entre as faixas etárias extremas — e serão mais impactados pelo envelhecimento?

---

## 📌 Principais achados

- A base da pirâmide etária encolheu significativamente entre 2000 e 2022, evidenciando queda na taxa de natalidade
- A faixa de 20 a 44 anos passou a predominar no Censo de 2022
- A região **Norte** concentra a maior proporção de pessoas com menos de 20 anos
- Os estados do **Sul e Sudeste** apresentam as maiores proporções de idosos e as menores diferenças entre jovens e idosos — indicando que serão os primeiros e mais afetados pelos impactos do envelhecimento na previdência e no mercado de trabalho

---

## 🗂️ Estrutura do projeto

```
analise-envelhecimento-ibge/
│
├── envelhecimento_brasil.ipynb   # Notebook principal com análise completa
├── codigo/
│   └── envelhecimento_brasil.py  # Versão .py do notebook
├── dados/
│   ├── populacao_por_sexo_idade_2000.csv
│   ├── populacao_por_sexo_idade_2010.csv
│   ├── populacao_por_sexo_idade_2022.csv
│   └── populacao_por_estado_2022.csv
└── json_files/
    └── brasil_estados.json       # GeoJSON para mapas coropléticos
```

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)

| Biblioteca | Uso |
|------------|-----|
| Pandas | Leitura, limpeza e transformação dos dados do IBGE |
| Matplotlib + Seaborn | Pirâmides etárias e gráficos comparativos |
| Plotly Express | Mapas coropléticos interativos por estado |

---

## ▶️ Como executar

**Pré-requisitos:** Python 3.8+ e Jupyter Notebook

```bash
# Clone o repositório
git clone https://github.com/guiccamargo/analise-envelhecimento-ibge.git
cd analise-envelhecimento-ibge

# Instale as dependências
pip install pandas matplotlib seaborn plotly jupyter

# Abra o notebook
jupyter notebook envelhecimento_brasil.ipynb
```

---

## 📂 Fonte dos dados

| Censo | Tabela IBGE (SIDRA) |
|-------|---------------------|
| 2000 | [Tabela 200](https://sidra.ibge.gov.br/tabela/200) |
| 2010 | [Tabela 1378](https://sidra.ibge.gov.br/tabela/1378) |
| 2022 | [Tabela 9514](https://sidra.ibge.gov.br/tabela/9514) |

---

## 👤 Autor

**Guilherme Camargo** — [@guiccamargo](https://github.com/guiccamargo)
