#Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

# Resposta: Outliers são valores que muito se afastam do padrão dos dados. Eles podem ser identificados usando métodos estatísticos como o desvio padrão ou os quartis.
    # Usando o desvio padrão, um valor é considerado um outlier se estiver a mais 3 desvios padrão da média como outlier.
    # Usando os quartis, um valor é considerado um outlier se estiver abaixo do primeiro quartil (Q1) menos 1.5 vezes o intervalo interquartil (IQR) ou acima do terceiro quartil (Q3) mais 1.5 vezes o IQR.
    # O IQR é a diferença entre Q3 e Q1.

import pandas as pd

df = pd.DataFrame({"valores": [10, 12, 12, 13, 12, 14, 13, 100, 12, 11, 13, 14, 15, 16, 14]})

# Desvio padrão
media = df["valores"].mean()
desvio_padrao = df["valores"].std()
limiar_superior = media + 3 * desvio_padrao
limiar_inferior = media - 3 * desvio_padrao
outliers = df[(df["valores"] > limiar_superior) | (df["valores"] < limiar_inferior)]

print("Outliers identificados usando desvio padrão:")
print(outliers)

# Quartis
Q1 = df["valores"].quantile(0.25)
Q3 = df["valores"].quantile(0.75)
IQR = Q3 - Q1
limiar_superior = Q3 + 1.5 * IQR
limiar_inferior = Q1 - 1.5 * IQR
outliers_quartis = df[(df["valores"] > limiar_superior) | (df["valores"] < limiar_inferior)]

print("Outliers identificados usando quartis:")
print(outliers_quartis)