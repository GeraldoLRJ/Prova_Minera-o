import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv('titanic.csv')

tita['Sobrevivente'] = tita['Survived']
tita['Sobrevivente'] = tita['Sobrevivente'].replace([1],'Sim')
tita['Sobrevivente'] = tita['Sobrevivente'].replace([0],'Nao')

tita = tita.head(10)
tita = tita.sort_values('Name')
print(tita)