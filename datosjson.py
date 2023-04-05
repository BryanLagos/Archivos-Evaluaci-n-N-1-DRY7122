import json

# Abrir el archivo JSON y leer su contenido en una variable
with open('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r') as file:
    json_file = json.load(file)

# Imprimir el contenido del archivo JSON
print(json_file)

