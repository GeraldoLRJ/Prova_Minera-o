import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv('titanic.csv')

tita = tita.sort_values('Name')
print(tita)