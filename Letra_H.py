import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv('titanic.csv')

tita['Survived'].fillna(1,inplace=True)
tita.drop(tita.loc[tita['Survived'] == 1].index,inplace=True)
titaG = tita.groupby('Sex', as_index = False)['Survived'].count()

print(titaG)