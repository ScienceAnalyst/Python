import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('/Users/Yomero/Documents/Encuestas y DB/Encuesta Nacional 2018/Antropometria.csv', encoding="ISO-8859-1")

filtro = datos['edad']>18
peso_adultos=datos[filtro]

#print(peso_adultos)

plt.figure(figsize=(7,7))
#plt.bar(peso_adultos['peso'], peso_adultos['edad'], label='Peso')
plt.legend(loc='upper right')
plt.show()
