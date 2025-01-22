# EDA e Análise de Crédito

Este projeto realiza uma análise exploratória e estatística de dados relacionados ao crédito de clientes, com o objetivo de identificar padrões de comportamento financeiro e insights valiosos para tomadas de decisão estratégicas.

## Funcionalidades
**- Limpeza de Dados:** Remoção de linhas com valores ausentes.
**- Análise Exploratória de Dados (EDA):**
    - Distribuição de gênero, faixa salarial e tipo de cartão.
    - Gastos médios por gênero, escolaridade, estado civil e número de dependentes.
    - Limite de crédito médio por tipo de cartão.
    - Correlações entre variáveis financeiras.
**- Visualizações Interativas:**
    - Gráficos de barras, pizza e heatmaps.
    - Representação clara das relações entre as variáveis.
**- Requisitos**
- Python 3.x
- Bibliotecas Python:
    - pandas
    - numpy
    - matplotlib
    - seaborn

Você pode instalar os requisitos executando:

```bash
pip install -r requirements.txt
```
Como usar
1. Clone o repositório:
```bash
git clone https://github.com/marques-viniciusc/eda-e-analise-de-credito
```
2. Instale as dependências:
```bash
pip install -r requirements.txt
````

3. Coloque o arquivo credito.csv no mesmo diretório do script.

4. Execute o script:
```bash
python eda-e-analise-de-credito.py
```

## Exemplos de Insights

**- Distribuição de Gênero:** A maioria dos clientes é do sexo masculino.

**- Gasto Médio por Gênero:** Mulheres gastam ligeiramente mais do que homens, mas a diferença é pequena.

**- Faixa Salarial:** A maioria dos clientes ganha menos de $40k por ano.

**- Tipo de Cartão:**
    - Cartões "blue" têm menor limite e gasto médio.
    - Cartões "gold" possuem os maiores valores de limite e gasto médio.
    
**- Dependentes:** Clientes com menos dependentes gastam mais.

## Observações
Certifique-se de que o arquivo credito.csv esteja formatado corretamente com as colunas esperadas e que as bibliotecas estejam atualizadas.
