import pandas as pd
import matplotlib.pyplot as plt

tita = pd.read_csv('titanic.csv')
tita = tita.drop(columns=['SibSp'])
tita = tita.drop(columns=['Parch'])
tita = tita.drop(columns=['Ticket'])

tita = tita.rename(columns = {'PassengerId': 'IdPassageiro', 'Survived': 'Sobrevivnetes', 'Pclass':'ClasseP', 'Name':'Nome','Sex':'Sexo', 'Age':'Idade', 'Fare':'Tarifa', 'Cabin':'Cabine', 'Embarked':'Embarcou'}, inplace = False)

tita = tita.head(10)

print(tita)