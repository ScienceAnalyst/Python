import csv

with open('C:\Users\Yomero\Documents\Proyecto_Py\ejemplo_csv.csv','w', encoding='utf-8') as filecsv:
    writer=csv.writer(filecsv)
    writer.writerow(['Nombre','Direccion','Telefono','CP'])
    writer.writerow(['Adan','Direccion1','Telefono1','CP1'])
    writer.writerow(['Rodrigo','Direccion2','Telefono2','CP2'])

with open('C:\Users\Yomero\Documents\Proyecto_Py\ejemplo_csv.csv','r', encoding='utf-8') as filecsv:
    reader = csv.reader(filecsv)
    for row in filecsv
        print(row)