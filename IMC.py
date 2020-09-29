import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/Yomero/Documents/Encuestas y DB/Encuesta Nacional 2018/Antropometria.csv', encoding="ISO-8859-1")
#print(df[['folio','desc_ent','peso',talla]])


#Elimina los 2 primeros caracteres
#res= [sub[2:] for sub in df['desc_ent']]
#print(res)

#Busca la cadena que contenga Colima
#Colima=df.loc[df['desc_ent'].str.contains('COLIMA')]
#print(Colima)

#Cambiar el tipo de dato de objeto a float
peso = df['peso']
p = pd.to_numeric(peso, errors='coerce')
p = p.dropna()

talla = df['talla']
t = pd.to_numeric(talla, errors='coerce')
t = t.dropna()

JAL = df.loc[(df['desc_ent']=="14 JALISCO")&(df['edad']>17)]
JAL['IMC']=p/((t*t)/10000)

plt.figure(figsize=(7,7))
#plt.scatter(JAL['edad'], JAL['IMC'], s=100)
#plt.bar(JAL['edad'], JAL['IMC'])
plt.hist(JAL['IMC'], bins=[18.5,25], rwidth=0.95, color='g')
plt.hist(JAL['IMC'], bins=[25,30], rwidth=0.95, color='r')
plt.hist(JAL['IMC'], bins=[30,40], rwidth=0.95, color='b')
plt.hist(JAL['IMC'], bins=[40,50], rwidth=0.95, color='black')
plt.show()

#print(JAL[['edad','peso','talla','IMC']].head(215))


#df['IMC']=df['peso']/(df['talla']*df['talla'])

#print(df['peso'])

#df.loc[df['IMC']<20]='Bajo Peso'
#df.loc[df['IMC']>40]='Sobre Peso'

#df.groupby(['desc_ent']).mean().sort_values('talla',ascending=False)

#for df in pd.read_csv('/Users/Yomero/Documents/Encuestas y DB/Encuesta Nacional 2018/Antropometria.csv', encoding="ISO-8859-1", chunksize=10):
#    print(peso.info())

#plt.figure(figsize=(7,7))
#plt.bar(limpia_datos['peso'], limpia_datos['edad'], label='X')
#plt.legend(loc='upper right')
#plt.show()

#altura = datos['talla']

#peso = pd.to_numeric(peso)
#altura = pd.to_numeric(altura)
#print(altura * peso)

#imc = peso/(altura*altura)

#imc = round(imc,1)

#print(imc)