try:
    import requests
    from bs4 import BeautifulSoup
    from bs4 import Comment
except ImportError:
    sys.exit("""Falta instalar algunos paquetes.
                Instalar mediante pip install -r requirements.txt""")

while(True):
    print("Escribe la url a ingresar: ")
    url = input()            
    try:
        req = requests.get(url, stream=True)
        break
    except requests.exceptions.RequestException as e:
        print(e)

html = ''
for line in req.iter_lines():
    if line: 
        html+=str(line)

soup = BeautifulSoup(html, "html.parser")
countScriptTags = 0
jsFindText = soup.findAll('script', type="text/javascript")

for tag in jsFindText:
    print(tag)
    countScriptTags+=1

print("Cantidad de tags javascript no comentados: " + str(countScriptTags))