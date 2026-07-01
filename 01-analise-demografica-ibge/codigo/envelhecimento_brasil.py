#!/usr/bin/env python
# coding: utf-8

# # Pirâmide Etária do Brasil ao longo do tempo

# Esta análise pretende oferecer um panorama geral da mudança na pirâmide etária brasileira, com base em três edições do Censo realizadas pelo IBGE em 2000, 2010 e 2022. Estes dados permitem uma visualização de como a média de idade dos brasileiros está subindo, o que pode implicar em uma falta de mão de obra e uma sobrecarga do sistema previdenciário. Em seguida, analisaremos quais estados brasileiros têm as maiores discrepâncias entre a quantidade de jovens e de idosos, considerando que esses estados serão mais afetados pela alteração da pirâmide etária.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
sns.set(style="darkgrid", palette="viridis", font_scale=1.2)


# Iremos começar construindo a pirâmide etária de cada um das três edições do Censo em análise.

# ## Censo 2000
# 
# Fonte: https://sidra.ibge.gov.br/tabela/200

# In[2]:


raw_data = pd.read_csv('./dados/populacao_por_sexo_idade_2000.csv', skiprows=5, skipfooter=14, engine='python')
df_2000 = raw_data.copy()


# In[3]:


df_2000.drop(index=0, inplace=True)
df_2000.reset_index(inplace=True, drop=True)
df_2000.rename(columns={'Grupo de idade': 'Idade'}, inplace=True)


# Convertendo valores numéricos

# In[4]:


df_2000['Homens'] = pd.to_numeric(df_2000['Homens']) * -1
df_2000['Mulheres'] =pd.to_numeric(df_2000['Mulheres'])


# In[5]:


df_2000 = df_2000[::-1]


# ### Construindo Pirâmide Etária

# In[6]:


fig, ax = plt.subplots(figsize=(8, 5))


plt.title('Pirâmide Populacional (%)\nBrasil 2000\n')
sns.barplot(data=df_2000, x='Homens', y='Idade', ax=ax, color='mediumseagreen', label='Homens')
sns.barplot(data=df_2000, x='Mulheres', y='Idade', ax=ax, color='orange', label='Mulheres')

# Ajustar sinal dos valores do gráfico
ticks = ax.get_xticks()
ax.set_xticks(ticks, [int(abs(tick)) if tick < 0 else int(tick) for tick in ticks])

ax.legend()
plt.tight_layout()
plt.show()


# ### O Censo de 2000 apresenta uma pirâmide etária relativamente equilibrada, com uma base mais larga e topo estreito

# ## Censo 2010
# 
# Fonte: https://sidra.ibge.gov.br/tabela/1378

# In[7]:


raw_data = pd.read_csv('./dados/populacao_por_sexo_idade_2010.csv', skiprows=7, skipfooter=14, engine='python')
df_2010 = raw_data.copy()


# ### Os intervalos de idade do censo 2010 tem que ser processados para serem comparados com o censo 2022

# Criando intervalo 15 a 19 anos

# In[8]:


idade_15_19 = df_2010.iloc[3:5]
homens_15_19 = round(sum(idade_15_19['Homens']), 2)
mulheres_15_19 = round(sum(idade_15_19['Mulheres']), 2)
df_2010.iloc[3] = {'Idade': '15 a 19 anos', 'Homens': homens_15_19, 'Mulheres': mulheres_15_19}
df_2010.drop(index=range(4, 5), inplace=True)
df_2010.reset_index(inplace=True, drop=True)


# Criando intervalo 80 a 84 anos

# In[9]:


idade_80_84 = df_2010.iloc[16:21]
homens_80_84 = round(sum(idade_80_84['Homens']), 2)
mulheres_80_84 = round(sum(idade_80_84['Mulheres']), 2)
df_2010.iloc[16] = {'Idade': '80 a 84 anos', 'Homens': homens_80_84, 'Mulheres': mulheres_80_84}
df_2010.drop(index=range(17, 21), inplace=True)
df_2010.reset_index(inplace=True, drop=True)


# Criando intervalo 85 a 89 anos

# In[10]:


idade_85_89 = df_2010.iloc[17:22]
homens_85_89 = round(sum(idade_85_89['Homens']), 2)
mulheres_85_89 = round(sum(idade_85_89['Mulheres']), 2)
df_2010.iloc[17] = {'Idade': '85 a 89 anos', 'Homens': homens_85_89, 'Mulheres': mulheres_85_89}
df_2010.drop(index=range(18, 22), inplace=True)
df_2010.reset_index(inplace=True, drop=True)


# Criando intervalo 90 a 94 anos

# In[11]:


idade_90_94 = df_2010.iloc[18:23]
homens_90_94 = round(sum(idade_90_94['Homens']), 2)
mulheres_90_94 = round(sum(idade_90_94['Mulheres']), 2)
df_2010.iloc[18] = {'Idade': '90 a 94 anos', 'Homens': homens_90_94, 'Mulheres': mulheres_90_94}
df_2010.drop(index=range(19, 23), inplace=True)
df_2010.reset_index(inplace=True, drop=True)


# Criando intervalo 95 a 99 anos

# In[12]:


idade_95_99 = df_2010.iloc[19:24]
homens_95_99 = round(sum(idade_95_99['Homens']), 2)
mulheres_95_99 = round(sum(idade_95_99['Mulheres']), 2)
df_2010.iloc[19] = {'Idade': '95 a 99 anos', 'Homens': homens_95_99, 'Mulheres': mulheres_95_99}
df_2010.drop(index=range(20, 24), inplace=True)
df_2010.reset_index(inplace=True, drop=True)


# Preparando dados para o gráfico

# In[13]:


df_2010 = df_2010[::-1]
df_2010['Homens'] = df_2010['Homens'] * -1


# ### Construindo Pirâmide Etária

# In[14]:


fig, ax = plt.subplots(figsize=(8, 5))


plt.title('Pirâmide Populacional (%)\nBrasil 2010\n')
sns.barplot(data=df_2010, x='Homens', y='Idade', ax=ax, color='mediumseagreen', label='Homens')
sns.barplot(data=df_2010, x='Mulheres', y='Idade', ax=ax, color='orange', label='Mulheres')

# Ajustar sinal dos valores do gráfico
ticks = ax.get_xticks()
ax.set_xticks(ticks, [int(abs(tick)) if tick < 0 else int(tick) for tick in ticks])

ax.legend()
plt.tight_layout()
plt.show()


# ### No Censo de 2010 notamos uma considerável redução na base da pirâmide, indicando uma queda na taxa de natalidade desde o último Censo

# ## Censo 2022
# Fonte https://sidra.ibge.gov.br/tabela/9514

# ### Importando dados excluindo cabeçalho e rodapé

# In[15]:


raw_data = pd.read_csv('./dados/populacao_por_sexo_idade_2022.csv', skiprows=6, skipfooter=14, engine='python')
df_2022 = raw_data.copy()


# ### Invertendo ordem das linhas

# In[16]:


df_2022 = df_2022[::-1]


# ### Invertendo sinal da coluna "Homens" para visualizar no gráfico

# In[17]:


df_2022['Homens'] = df_2022['Homens'] * -1


# ### Construindo Pirâmide Etária

# In[18]:


fig, ax = plt.subplots(figsize=(8, 5))


plt.title('Pirâmide Populacional (%)\nBrasil 2022\n')
sns.barplot(data=df_2022, x='Homens', y='Idade', ax=ax, color='mediumseagreen', label='Homens')
sns.barplot(data=df_2022, x='Mulheres', y='Idade', ax=ax, color='orange', label='Mulheres')

# Ajustar sinal dos valores do gráfico
ticks = ax.get_xticks()
ax.set_xticks(ticks, [int(abs(tick)) if tick < 0 else int(tick) for tick in ticks])

ax.legend()
plt.tight_layout()
plt.show()


# ### No Censo de 2022, notamos uma redução da base da pirâmide e uma predominância da população entre 20 e 44 anos.

# ### Alterações nos extremos da pirâmide

# In[19]:


menos_de_vinte_2000 = df_2000.iloc[17:]['Mulheres'].sum() - df_2000.iloc[17:]['Homens'].sum()
menos_de_vinte_2010 = df_2010.iloc[17:]['Mulheres'].sum() - df_2010.iloc[17:]['Homens'].sum()
menos_de_vinte_2022 = df_2022.iloc[17:]['Mulheres'].sum() - df_2022.iloc[17:]['Homens'].sum()

with sns.axes_style("darkgrid"):
    plt.figure(figsize=(8, 5))
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    fig = sns.barplot(x=[2000, 2010, 2022], y=[menos_de_vinte_2000, menos_de_vinte_2010, menos_de_vinte_2022])
    fig.set_xlabel('Censo', fontsize=14)
    fig.set_ylabel('População', fontsize=14)
    plt.title('Pessoas com Menos de 20 Anos', fontsize=16)
    fig.set_ylim(0, 100)
    plt.tight_layout()
    plt.show()


# ## Notamos uma redução considerável na parcela da população com menos de 20 anos

# In[20]:


idosos_2000 = df_2000.iloc[:9]['Mulheres'].sum() - df_2000.iloc[17:]['Homens'].sum()
idosos_2010 = df_2010.iloc[:9]['Mulheres'].sum() - df_2010.iloc[17:]['Homens'].sum()
idosos_2022 = df_2022.iloc[:9]['Mulheres'].sum() - df_2022.iloc[17:]['Homens'].sum()

with sns.axes_style("darkgrid"):
    plt.figure(figsize=(8, 5))
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    fig = sns.barplot(x=[2000, 2010, 2022], y=[idosos_2000, idosos_2010, idosos_2022], color='green')
    fig.set_xlabel('Censo', fontsize=14)
    fig.set_ylabel('População', fontsize=14)
    plt.title('Idosos', fontsize=16)
    fig.set_ylim(0, 100)
    plt.tight_layout()
    plt.show()


# ## Não parece haver mudança considerável na parcela da população com mais de 60 anos

# In[21]:


menos_de_vinte_2000 = df_2000.iloc[17:]['Mulheres'].sum() - df_2000.iloc[17:]['Homens'].sum()
menos_de_vinte_2010 = df_2010.iloc[17:]['Mulheres'].sum() - df_2010.iloc[17:]['Homens'].sum()
menos_de_vinte_2022 = df_2022.iloc[17:]['Mulheres'].sum() - df_2022.iloc[17:]['Homens'].sum()

with sns.axes_style("darkgrid"):
    plt.figure(figsize=(8, 5))
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    fig = sns.barplot(x=[2000, 2010, 2022], y=[menos_de_vinte_2000, menos_de_vinte_2010, menos_de_vinte_2022])
    fig.set_xlabel('Censo', fontsize=14)
    fig.set_ylabel('População', fontsize=14)
    plt.title('Pessoas com Menos de 20 Anos', fontsize=16)
    fig.set_ylim(0, 100)
    plt.tight_layout()
    plt.show()


# ## Comparando os dados dos Censos, notamos um achatamento da pirâmide etária, com uma notável redução da parcela da população com menos de 20 anos enquanto a população com mais de 60 anos se mantém acima de 20%.

# In[22]:


fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(18, 7), constrained_layout=True)

fig.suptitle('\nAchatamento da Pirâmide Etária Brasileira\n', fontsize=18)

ax3.set_title('Pirâmide Populacional (%)\nBrasil 2022\n')
sns.barplot(data=df_2022, x='Homens', y='Idade', ax=ax3, color='mediumseagreen', label='Homens')
sns.barplot(data=df_2022, x='Mulheres', y='Idade', ax=ax3, color='orange', label='Mulheres')

# Ajustar sinal dos valores do gráfico
ticks = ax3.get_xticks()
ax3.set_xticks(ticks, [int(abs(tick)) if tick < 0 else int(tick) for tick in ticks])

ax3.legend(loc='upper left')

ax2.set_title('Pirâmide Populacional (%)\nBrasil 2010\n')
sns.barplot(data=df_2010, x='Homens', y='Idade', ax=ax2, color='mediumseagreen', label='Homens')
sns.barplot(data=df_2010, x='Mulheres', y='Idade', ax=ax2, color='orange', label='Mulheres')

# Ajustar sinal dos valores do gráfico
ticks = ax2.get_xticks()
ax2.set_xticks(ticks, [int(abs(tick)) if tick < 0 else int(tick) for tick in ticks])

ax2.legend(loc='upper left')

ax1.set_title('Pirâmide Populacional (%)\nBrasil 2000\n')
sns.barplot(data=df_2000, x='Homens', y='Idade', ax=ax1, color='mediumseagreen', label='Homens')
sns.barplot(data=df_2000, x='Mulheres', y='Idade', ax=ax1, color='orange', label='Mulheres')

# Ajustar sinal dos valores do gráfico
ticks = ax1.get_xticks()
ax1.set_xticks(ticks, [int(abs(tick)) if tick < 0 else int(tick) for tick in ticks])

ax1.legend(loc='upper left')

plt.show()


# ## População por Estado

# In[23]:


raw_data = pd.read_csv('./dados/populacao_por_estado_2022.csv', skiprows=4, skipfooter=20, engine='python')
df_estados = raw_data.copy()
df_estados.set_index('Unidade da Federação', inplace=True)


# In[24]:


menores_de_vinte_anos = df_estados.iloc[:, 0:4]
adultos = df_estados.iloc[:, 4:9]
idosos = df_estados.iloc[:, -2:]


# In[25]:


menores_de_vinte_anos = menores_de_vinte_anos.sum(axis=1)
adultos = adultos.sum(axis=1)
idosos = idosos.sum(axis=1)


# In[26]:


menores_de_vinte_anos = pd.DataFrame(menores_de_vinte_anos, columns=['Populacao'])
idosos = pd.DataFrame(idosos, columns=['Populacao'])


# In[27]:


estados_brasileiros = {
    'Acre': 'AC',
    'Alagoas': 'AL',
    'Amapá': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceará': 'CE',
    'Distrito Federal': 'DF',
    'Espírito Santo': 'ES',
    'Goiás': 'GO',
    'Maranhão': 'MA',
    'Mato Grosso': 'MT',
    'Mato Grosso do Sul': 'MS',
    'Minas Gerais': 'MG',
    'Pará': 'PA',
    'Paraíba': 'PB',
    'Paraná': 'PR',
    'Pernambuco': 'PE',
    'Piauí': 'PI',
    'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN',
    'Rio Grande do Sul': 'RS',
    'Rondônia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'São Paulo': 'SP',
    'Sergipe': 'SE',
    'Tocantins': 'TO'
}


# In[28]:


codigos = [estados_brasileiros[estado] for estado in menores_de_vinte_anos.index.values]


# In[29]:


menores_de_vinte_anos['Estado'] = codigos
adultos['Estado']= codigos
idosos['Estado'] = codigos


# In[30]:


import json
geojson = json.load(open('./json_files/brasil_estados.json'))


# In[31]:


import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'notebook'


# In[32]:


fig_choropleth = px.choropleth(menores_de_vinte_anos, 
                               geojson=geojson, 
                               color_continuous_scale='Reds',
                               color='Populacao',
                               locations='Estado',
                               scope='south america',
                               title='Pessoas Menores de 20 Anos (%)')

fig_choropleth.update_layout(
    coloraxis_colorbar_title_text = 'População',
)
fig_choropleth.show()


# ## A região Norte do Brasil tem a maior contentração de pessoas com menos de 20 Anos

# In[33]:


fig_choropleth = px.choropleth(idosos, 
                               geojson=geojson, 
                               color_continuous_scale='Reds',
                               color='Populacao',
                               locations='Estado',
                               scope='south america',
                               title='Idosos (%)'
                   )

fig_choropleth.update_layout(
    coloraxis_colorbar_title_text = 'População'
)
fig_choropleth.show()


# ## Os estados do sul tem maior concentração de idosos em suas populações

# In[34]:


discrepancia = pd.DataFrame(menores_de_vinte_anos['Populacao'] - idosos['Populacao'])
discrepancia['Estado'] = idosos['Estado']


# In[35]:


fig_choropleth = px.choropleth(discrepancia, 
                               geojson=geojson, 
                               color_continuous_scale='Greens',
                               color='Populacao',
                               locations='Estado',
                               scope='south america',
                               title='Diferença entre porcentagem de jovens e idosos (%)'
                   )

fig_choropleth.update_layout(
    coloraxis_colorbar_title_text = 'População'
)
fig_choropleth.show()


# ## Estados com menores diferenças entre a porcentagem de jovens e idosos

# In[36]:


for estado in discrepancia.sort_values(by='Populacao').head().index:
    print(f'{estado}: {round(discrepancia.loc[estado]["Populacao"], 1)}%')


# ## A análise sugere que os estados das regiões sul e sudeste são os mais afetados pela diferença entre jovens e idosos, indindicando que estes estados serão mais impactados pelos efeitos do envelechimento da população.
