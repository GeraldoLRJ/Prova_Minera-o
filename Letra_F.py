import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv('titanic.csv')

tita['Sex'] = tita['Sex'].replace(['male'],'masculino')
tita['Sex'] = tita['Sex'].replace(['female'],'FEMININO')

tita = tita.head(10)
print(tita['Sex'])