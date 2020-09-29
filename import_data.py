import requests
import re

response = requests.get('https://www.upiig.ipn.mx/conocenos/directorio.html')

print(response.text)

result = re.findall(r'^\w+@\w+.\w+',response.text)

print(result)