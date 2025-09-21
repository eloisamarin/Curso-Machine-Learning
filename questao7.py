#Como concatenar vários DataFrames (empilhando linhas ou colunas),mesmo que tenham colunas diferentes?
#Resposta: Para concatenar vários DataFrames empilhando linhas ou colunas, mesmo que tenham colunas diferentes, usando a função pd.concat() do pandas.
#Para empilhar linhas, use axis=0 (padrão) e para empilhar  colunas, use axis=1. Se os DataFrames tiverem colunas diferentes, as colunas ausentes serão preenchidas com NaN.  


import pandas as pd

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "C": [7, 8]})

# Empilhando linhas
df_linhas = pd.concat([df1, df2], axis=0)
print("DataFrame empilhando linhas:")
print(df_linhas)
# Empilhando colunas
df_colunas = pd.concat([df1, df2], axis=1)
print("DataFrame empilhando colunas:")
print(df_colunas)       

