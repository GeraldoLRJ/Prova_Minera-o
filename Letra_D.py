import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv('titanic.csv')
tita = tita.drop(columns=['SibSp'])
tita = tita.drop(columns=['Parch'])
tita = tita.drop(columns=['Ticket'])

tita = tita.head(10)
print(tita)