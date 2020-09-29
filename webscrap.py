from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://es.wikibooks.org/wiki/Wikilibros:Libros_por_tem%C3%A1tica"
html_doc=urlopen(url)

soup=BeautifulSoup(html_doc,'html.parser')

temas=soup.find_all('span',{'class':'mw-headline'})

for tema in temas:
    print(tema)

