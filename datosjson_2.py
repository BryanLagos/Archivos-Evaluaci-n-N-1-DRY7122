import json

# Abrir el archivo JSON y cargarlo en un string
with open('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r') as file:
    ourjson = json.load(file)

# Imprimir el contenido del string ourjson
print(ourjson)
