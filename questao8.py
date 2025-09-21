#Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?
#Resposta: Para ler um arquivo CSV em um DataFrame e exibir as primeiras linhas pode ser usada a função pd.read_csv() do pandas e o método head().

import pandas as pd


df = pd.read_csv("arquivo.csv")  # "arquivo.csv" pelo caminho do seu arquivo CSV
print(df.head()) # Exibe as primeiras 5 linhas do DataFrame