import sys
import requests

print("Escribe la url a ingresar: "
url = input()
req = requests.get(url, stream=True)

for line in req.iter_lines():
    if line: print(line)