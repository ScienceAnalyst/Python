
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import os
import csv

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, 'chromedriver')

driver = webdriver.Chrome()
driver.get("https://fbref.com/es/comps/31/479/Estadisticas-2010-2011-Primera-Division")
elements= driver.find_elements_by_xpath("//href[text()='America']")#elemento_busqueda = "min_width sortable stats_table now_sortable"
try:
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, elemento_busqueda)))
    #waits 10 seconds until element is located. Can have other wait conditions  such as visibility_of_element_located or text_to_be_present_in_element
    #driver.implicitly_wait(10)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    
    Jugadores = soup.find_all("table", {"id":"stats_standard_479"})
    Precio = soup.find_all("table", {"id":"stats_shooting_479"})

    #lista=[{'id':index, 'descripcion':Descripciones[index].text, 'precio_art':Precio[index].p.text} for index in range(len(Descripciones)-1)]    
    with open('articulos_precio.csv','w+') as filecsv:
            writer=csv.DictWriter(filecsv)#, fieldnames=['id','Desc','Precio'])
            writer.writeheader()
            #for producto in lista:
            #writer.writerow(producto)
  
except Exception as e:
    print(e)
finally:
    driver.quit()