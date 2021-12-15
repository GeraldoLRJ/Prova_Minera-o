import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv('titanic.csv')

tita['Survived'].fillna(0,inplace=True)
tita.drop(tita.loc[tita['Survived'] == 0].index,inplace=True)
titaG = tita.groupby('Pclass', as_index = False)['Survived'].count()

plt.bar(titaG['Pclass'], titaG['Survived'])
plt.show()

print(titaG)