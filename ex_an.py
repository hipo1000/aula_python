import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# 1. Importação dos Dados
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[ :, :-1 ].values
y = dataset.iloc[ :, -1 ].values

# 2. Tratamento de Valores Ausentes (Imputação)
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# 3. Tratamento de Dados Categóricos (Label Encoding)
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0]) 

# --- COMANDOS PARA APRESENTAR AS TABELAS ---

print("--- Matriz de Features (X) após Imputação e Label Encoding ---")
print(X)
print("\n--- Vetor de Variável Dependente (y) ---")
print(y)
