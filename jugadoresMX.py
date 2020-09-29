import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv('/Users/Yomero/Documents/Proyecto_Py/ligamx2010_atlas.csv', skiprows=6,encoding="utf-8")
limpia_datos = datos.dropna(subset=['Edad'])
plt.figure(figsize=(7,7))
plt.scatter(limpia_datos['PJ'], limpia_datos['Jugador'], color='b', s=100, label='Juegos de Cambio')
plt.scatter(limpia_datos['Titular'], limpia_datos['Jugador'], color='y', s=100, label='Juegos de Inicio')
plt.legend(loc='upper right')
plt.show()