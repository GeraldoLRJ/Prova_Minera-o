import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv('titanic.csv')

titaex=pd.ExcelWriter('Titanicex.xlsx')
tita.to_excel(titaex, index = False)
titaex.save()