# Pegar informações sobre o dataframe
df.describe()<br>
- Métricas de tendência central e dispersão<br>

df.shape<br>
- Traz o número de linhas e colunas do DataFrame<br>

df.info

df.dtypes
- Retorna o tipo dos valores de cada coluna

# Renomear index
df.columns.name = 'indice'
- Utilizado para deixar o DataFrame mais limpo

# Chamar uma coluna
df.nomedacoluna<br>
exemplo['nomedacoluna']

# Recortar DataFrame
df.loc[]
- Recorta pelo nome do index

df.iloc[]
- Recorta pelo valor do indice

df[]
- Recorta pelo nome da coluna

df[:]
- Recorta pelo indice da linha e da coluna

df.coluna
- Recorta pelo nome da coluna

# Tratamento de dados faltantes
df.isnull()
- Retorna True caso seja dado faltante

df.dropna(subset = 'nome da coluna')
- Retorna o df com os valores nulos dropados. Nao esquecer do argumento inplace = True

df.fillna()
