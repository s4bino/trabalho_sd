import requests
import json

# Carregue o arquivo JSON
with open('dados.json', 'r') as f:
    data = json.load(f)

# Envie a requisição POST para o servidor
response = requests.post('http://localhost:3000/api/produtos', json=data)

# Imprima a resposta do servidor
print(response.text)