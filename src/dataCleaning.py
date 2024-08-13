from bs4 import BeautifulSoup
import json
import sched
import time
import requests

# Função de limpeza de dados
def dataCleaning():
    nome_arquivo = "src/pageCompras.html"

    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')
    produtos = soup.find_all('div', class_='promocao-produtos-item')
    lista_produtos = []

    for produto in produtos:
        produto_nome = produto.find('div', class_='promocao-item-nome').get_text(strip=True)
        produto_preco = produto.find('div', class_='promocao-item-preco-oferta').find('strong').get_text(strip=True)
        loja_nome = produto.find('div', class_='promocao-item-border').find('img', class_='lozad')['alt']

        produto_obj = {
            "nome": produto_nome,
            "preco": produto_preco,
            "loja": loja_nome
        }
        lista_produtos.append(produto_obj)

    return lista_produtos

# Configuração do scheduler
scheduler = sched.scheduler(time.time, time.sleep)

def agendar(intervalo):
    lista_produtos = dataCleaning()
    enviar(lista_produtos)
    scheduler.enter(intervalo, 1, agendar, (intervalo,))

def enviar(lista_produtos):
    # Envie a requisição POST para o servidor
    response = requests.post('http://localhost:3000/api/produtos', json=lista_produtos)

    # Imprima a resposta do servidor
    print(response.text)

# Intervalo de tempo entre execuções em segundos
intervalo = 5

# Iniciar o agendamento
scheduler.enter(0, 1, agendar, (intervalo,))
scheduler.run()
