#Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
#Resposta: Para lidar com valores ausentes (NaN) em um DataFrame, você pode usar os métodos dropna() para remover linhas ou colunas com NaN, fillna() para preencher NaN com um valor específico, ou isna() para identificar onde os valores ausentes estão localizados.

import pandas as pd
import numpy as np
df = pd.DataFrame({
    "A": [1, 2, np.nan, 4],
    "B": [np.nan, 2, 3, 4],
    "C": [1, np.nan, np.nan, 4] 
})
print("DataFrame original:")
print(df)

# Removendo linhas com NaN
df_sem_nan = df.dropna() 
print("DataFrame sem NaN:")
print(df_sem_nan)

# Preenchendo NaN com um valor específico
df_preenchido = df.fillna(0) # Preenche NaN com 0
print("DataFrame preenchido:")
print(df_preenchido)

# Identificando onde estão os NaN
print("Localização dos NaN:")
print(df.isna()) # Retorna um DataFrame booleano indicando a presença de NaN