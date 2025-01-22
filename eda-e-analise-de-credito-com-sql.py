'''
# Análise Exploratória (EDA) e Análise de crédito usando SQL
Análise Exploratória (EDA) e Análise de Crédito Este projeto visa realizar uma análise exploratória e estatística de um conjunto de dados fictício relacionado a informações de clientes, como idade, escolaridade, estado civil, faixa salarial e comportamento de consumo. A análise tem como objetivo identificar padrões e insights relevantes que possam auxiliar na criação de estratégias de crédito e políticas financeiras mais eficazes.

Além disso, exploramos a relação entre diferentes variáveis como gênero, escolaridade, tipo de cartão, dependentes e limite de crédito, com o intuito de entender melhor o perfil dos clientes e os fatores que influenciam seu comportamento financeiro.

---------------------------------------------------------------
Objetivos:

- Explorar e limpar os dados para garantir sua integridade e qualidade.
- Analisar correlações entre variáveis demográficas e financeiras.
- Visualizar os padrões de comportamento de crédito e consumo através de gráficos.
- Identificar insights valiosos para decisões estratégicas.
---------------------------------------------------------------
'''

# Importação de bibliotecas

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Extração dos dados e visualização inicial dos dados

nomes_das_colunas = ['idade', 'sexo', 'dependentes', 'escolaridade', 'estado_civil', 'salario_anual', 'tipo_cartao', 'qtd_produtos',
             'iteracoes_12m', 'meses_inativo_12m', 'limite_credito', 'valor_transacoes_12m', 'qtd_transacoes_12m']
data = pd.read_csv('credito.csv', names=nomes_das_colunas)

print(data.head())

# Análise Exploratória de Dados (EDA)

print(data.info()) # Visualização dos tipos de dados e da quantidade de linhas

pd.set_option('display.max_colwidth', None)  # Exibir todas as colunas sem limite de largura

print(data[['escolaridade', 'estado_civil', 'salario_anual', 'tipo_cartao']].apply(lambda col: col.unique())) # Análise dos valores únicos

data_limpo = data[~data.isin(['na']).any(axis=1)] # Remoção de colunas com valores nulos

print(data_limpo.info()) # Nova visualização para verificar se os valores nulos foram removidos

# Análise de Dados

## Média de idade por sexo

media_de_idade_por_sexo = data.groupby('sexo')['idade'].mean()

for genero in media_de_idade_por_sexo.index:
    print(f'A média de idade para o gênero {genero} é {media_de_idade_por_sexo[genero]:.2f}')

plt.figure(figsize=(10, 6))
plt.pie(data['sexo'].value_counts(), labels=data['sexo'].value_counts().index, colors=['dodgerblue', 'hotpink'],  autopct='%1.1f%%')
plt.title('Distribuição de Gênero')
plt.show()

### Insight: podemos observar que a maioria dos clientes é do sexo masculino.

## Média de gasto por sexo

media_de_gastos_por_sexo = data.groupby('sexo')['valor_transacoes_12m'].mean()

for genero in media_de_gastos_por_sexo.index:
    print(f'A média de gastos para o gênero {genero} é {media_de_gastos_por_sexo[genero]:.2f}')

plt.figure(figsize=(10, 6))
plt.bar(media_de_gastos_por_sexo.index, media_de_gastos_por_sexo, color=['dodgerblue', 'hotpink'])
plt.title('Média de Gastos por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Média de Gastos')
plt.show()

### Insight: notamos que as mulheres gastam ligeiramente a mais do que homens, no entanto, a diferença é irrisória.

## Quantidade por faixa salarial

salario_anual = data_limpo['salario_anual'].value_counts() # Contagem de valores únicos

salario_anual = salario_anual.sort_index() # Ordenação dos valores
print(salario_anual)

plt.figure(figsize=(10, 6))
sns.barplot(x=salario_anual.index, y=salario_anual.values, palette='viridis', hue=salario_anual.index, legend=False)
plt.title('Distribuição de Faixas Salariais', fontsize=16)
plt.xlabel('Faixa Salarial', fontsize=12)
plt.ylabel('Quantidade de Pessoas', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


### Insight: a maioria dos clientes tem um salário anual inferior a 40k, e uma pequena parcela tem um salário anual superior a 120k.

## Média de idade por faixa salarial

media_idade_por_salario = data_limpo.groupby('salario_anual')['idade'].mean().round(2)
print(media_idade_por_salario)

plt.figure(figsize=(10, 6))
sns.barplot(x=media_idade_por_salario.index, y=media_idade_por_salario.values, palette='viridis', hue=media_idade_por_salario.index, legend=False)
plt.title('Média de Idade por Faixa Salarial', fontsize=16)
plt.xlabel('Faixa Salarial', fontsize=12)
plt.ylabel('Média de Idade', fontsize=12)
plt.xticks(rotation=45) # rotação dos rótulos
plt.tight_layout() # ajuste para o gráfico não ser cortado
plt.show()

### Insight: não parece haver correlação entre idade e faixa salarial.

## Gasto por escolaridade

gasto_por_escolaridade = data_limpo.groupby('escolaridade')['valor_transacoes_12m'].mean().round(2)
print(gasto_por_escolaridade)

plt.figure(figsize=(10, 6))
sns.barplot(x=gasto_por_escolaridade.index, y=gasto_por_escolaridade.values, palette='viridis', hue=gasto_por_escolaridade.index, legend=False)
plt.title('Gasto por Escolaridade', fontsize=16)
plt.xlabel('Escolaridade', fontsize=12)
plt.ylabel('Média de Gastos', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Insight: também não parece haver correlação entre gasto e escolaridade.

## Gasto por estado civil

gasto_por_estado_civil = data_limpo.groupby('estado_civil')['valor_transacoes_12m'].mean().round(2)
print(gasto_por_estado_civil)

plt.figure(figsize=(10, 6))
sns.barplot(x=gasto_por_estado_civil.index, y=gasto_por_estado_civil.values, palette='viridis', hue=gasto_por_estado_civil.index, legend=False)
plt.title('Gasto por Estado Civil', fontsize=16)
plt.xlabel('Estado Civil', fontsize=12)
plt.ylabel('Média de Gastos', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Insight: a correlação entre gasto e estado civil parece ser muito baixa, com pessoas casadas gastando ligeiramente menos do que divorciados e solteiros.

## Gasto por dependentes

gasto_por_dependentes = data_limpo.groupby('dependentes')['valor_transacoes_12m'].mean().round(2)
print(gasto_por_dependentes)

plt.figure(figsize=(10, 6))
sns.barplot(x=gasto_por_dependentes.index, y=gasto_por_dependentes.values, palette='viridis', hue=gasto_por_dependentes.index, legend=False)
plt.title('Gasto por Dependentes', fontsize=16)
plt.xlabel('Número de Dependentes', fontsize=12)
plt.ylabel('Média de Gastos', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Insight: a correlação entre gasto e número de dependentes é um pouco maior, com pessoas com menos dependentes sendo as que mais gastam e as pessoas com mais dependentes gastando menos.

## Limite de crédito por tipo de cartão

limite_por_cartao = data_limpo.groupby('tipo_cartao')['limite_credito'].mean().round(2)
print(limite_por_cartao)

plt.figure(figsize=(10, 6))
sns.barplot(x=limite_por_cartao.index, y=limite_por_cartao.values, palette='viridis', hue=limite_por_cartao.index, legend=False)
plt.title('Limite de Crédito por Tipo de Cartão', fontsize=16)
plt.xlabel('Tipo de Cartão', fontsize=12)
plt.ylabel('Limite de Crédito', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Insight: neste caso, parece haver uma forte correlação, já que pessoas com cartão blue possuem um limite médio de 8k, enquanto pessoas com cartão silver cerca de 24k e gold 28k.

## Gasto por tipo de cartão

gasto_por_cartao = data_limpo.groupby('tipo_cartao')['valor_transacoes_12m'].mean().round(2)
print(gasto_por_cartao)

plt.figure(figsize=(10, 6))
sns.barplot(x=gasto_por_cartao.index, y=gasto_por_cartao.values, palette='viridis', hue=gasto_por_cartao.index, legend=False)
plt.title('Gasto por Tipo de Cartão', fontsize=16)
plt.xlabel('Tipo de Cartão', fontsize=12)
plt.ylabel('Média de Gastos', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Insight: da mesma forma, o gasto por tipo de cartão parece seguir o mesmo padrão com cartões blue (gastam menos) e gold (gastam mais). Os cartões silver possuem gasto muito próximo ao cartão blue.

'''
# Conclusão

O trabalho acima busca demonstrar uma das análises possíveis feitas a partir dos dados da empresa. Novos dados e insights podem ser elaborados a partir de novas informações e diferentes abordagens.

Com as informações que temos, concluímos que:

Há mais clientes homens do que mulheres;
- A maioria dos clientes é do sexo masculino.
- Mulheres gastam ligeiramente mais do que homens, mas a diferença é pequena.
- A maioria dos clientes tem um salário anual inferior a 40k, e uma pequena parcela tem um salário anual superior a 120k.
- Não há correlação entre idade e faixa salarial.
- Não há correlação entre gasto e escolaridade.
- A correlação entre gasto e estado civil é baixa, com pessoas casadas gastando ligeiramente menos do que divorciados e solteiros.
- A correlação entre gasto e número de dependentes é um pouco maior, com pessoas com menos dependentes sendo as que mais gastam e as pessoas com mais dependentes gastando menos.
- Há uma forte correlação entre limite de crédito e tipo de cartão, com pessoas com cartão blue possuindo um limite médio de 8k, enquanto pessoas com cartão silver cerca de 24k e gold 28k.
- O gasto por tipo de cartão segue o mesmo padrão, com cartões blue gastando menos, cartões silver gastando um pouco mais e cartões gold gastando mais.
'''