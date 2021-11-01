# Pegar informações sobre o dataframe
.describe()<br>
- Métricas de tendência central e dispersão<br>

.shape<br>
- Traz o número de linhas e colunas do DataFrame<br>

.info

exemplo.dtypes
- Retorna o tipo dos valores de cada coluna

# Renomear index
exemplo.columns.name = 'indice'
- Utilizado para deixar o DataFrame mais limpo

# Chamar uma coluna
exemplo.nomedacoluna<br>
exemplo['nomedacoluna']

# Recortar DataFrame
exemplo.loc[]
- Recorta pelo nome do index

exemplo.iloc[]
- Recorta pelo valor do indice

exemplo[]
- Recorta pelo nome da coluna

exemplo[:]
- Recorta pelo indice da linha e da coluna

exemplo.
- Recorta pelo nome da coluna
