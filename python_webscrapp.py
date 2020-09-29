import requests
import csv
from bs4 import BeautifulSoup as bs

url = requests.get("https://fbref.com/es/equipos/c9d59c6c/2011-2012/Estadisticas-de-UNAM")

soup = bs(url.content,'html.parser')

filename = 'ligamx2012old.csv'

csv_writer = csv.writer(open(filename,'w', encoding="utf-8"))

Estadistica_anual=soup.find('table',id='stats_standard_546')

for tr in Estadistica_anual('tr'): #soup.find_all('tr'):
    data = []

    for th in tr.find_all('th'):
        data.append(th.text)
    
    if data:
        print("Iserting headers: {}".format(','.join(data)))
        csv_writer.writerow(data)
        
    for td in tr.find_all('td'):
        data.append(td.text.strip())
    if data:
        print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)#aqui termina el original scrap:

