import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("/Users/Yomero/Documents/Proyecto_Py/ligamx2010_estadistica_anual.csv", skiprows=6, encoding="utf-8")
limpia_datos = datos.dropna(subset=['PL'])
plt.figure(figsize=(7,7))
#plt.scatter(limpia_datos['Equipo'], limpia_datos['PL'], s=200)
plt.bar(limpia_datos['Equipo'], limpia_datos['PL'])
plt.xticks(limpia_datos['Equipo'], rotation='vertical')
plt.axhline(y=30, color='r')
plt.show()