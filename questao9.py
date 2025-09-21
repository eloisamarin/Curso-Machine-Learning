# Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
#Resposta: Para selecionar uma coluna específica em um DataFrame, pode usar a notação de colchetes ou o atributo de ponto. Para filtrar linhas com base em uma condição, você pode usar a indexação booleana.

import pandas as pd

df = pd.DataFrame({
    "Nome": ["Ana", "Luisa", "Paulo", "Maria"],
    "Idade": [23, 35, 45, 28],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
})

# Selecionando a coluna "Nome"
nomes = df["Nome"]
print("Coluna 'Nome':")
print(nomes)

# Filtrando linhas onde a idade é maior que 30
maior_que_30 = df[df["Idade"] > 30]
print("Pessoas com mais de 30 anos:")
print(maior_que_30)
# Filtrando linhas onde a cidade é "Curitiba"
curitiba = df[df["Cidade"] == "Curitiba"]
print("Pessoas que moram em Curitiba:")
print(curitiba) 
