import re
import requests
from bs4 import BeautifulSoup

print("Escribe la url a ingresar: ")
url = input()
req = requests.get(url, stream=True)

html = ''
for line in req.iter_lines():
    if line: 
        html+=str(line)

soup = BeautifulSoup(html, "html.parser")
countScriptTags = 0
jsFindText = soup.findAll('script', type="text/javascript")

for tag in jsFindText:
    countScriptTags+=1

print("Cantidad de tags javascript no comentados: " + str(countScriptTags))

