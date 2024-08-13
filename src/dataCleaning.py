from bs4 import BeautifulSoup
import json
import sched
import time
import requests
import subprocess

def dataCleaning(url):
    data = {}
    try:
        # Verifica se a URL é válida
        if not url:
            raise ValueError("A URL não pode ser vazia.")
        
        # Nome do arquivo onde o conteúdo HTML será salvo
        pageCompras = "pageCompras.html"
        
        # Executa o comando curl para obter o conteúdo da URL
        subprocess.run(['curl', '-o', pageCompras, url], check=True, text=True, capture_output=True)

        with open(pageCompras, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Extraindo o título do produto
        title = soup.find('div', class_='header-product-info--title').h2.text.strip()

        # Extraindo os preços
        prices = soup.find('div', class_='header-product-info--price').find_all('span')
        price_usd_min = prices[0].text.strip()
        price_usd_max = prices[1].text.strip()

        # Extraindo preços em diferentes moedas
        currency_elements = soup.find('div', class_='header-product-info--currency').find_all('span')
        price_brl = currency_elements[0].text.strip()
        price_ars = currency_elements[1].text.strip()
        
        dolar_cotacao = soup.find('span', class_='txt-quotation').strong.text.strip()


        data = {
            'title': title,
            'price_usd_min': price_usd_min,
            'price_usd_max': price_usd_max,
            'price_brl': price_brl,
            'price_ars': price_ars,
            'dolar_cotacao': dolar_cotacao
        }

        return data

    except Exception as e:
        print(f"Erro ao analisar o HTML: {e}")
    
    return data

# Configuração do scheduler
scheduler = sched.scheduler(time.time, time.sleep)

def agendar(intervalo):
    print(pedeLink())
    lista_produtos = dataCleaning(pedeLink())
    enviar(lista_produtos)
    scheduler.enter(intervalo, 1, agendar, (intervalo,))

def pedeLink():
    response = requests.get('http://localhost:3000/pedeLink')
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        return response.text  # Retorna o conteúdo da resposta, que é o link
    else:
        return None  # Ou você pode lidar com o erro de outra maneira

def enviar(lista_produtos):
    try:
        # Envie a requisição POST para o servidor
        response = requests.post('http://localhost:3000/api/produtos', json=lista_produtos)

        # Imprima a resposta do servidor
        print(response.text)
    except requests.exceptions.RequestException as e:
        # Caso ocorra um erro ao tentar enviar a requisição
        print(f"Erro ao tentar enviar a requisição: {e}")
    
# Intervalo de tempo entre execuções em segundos
intervalo = 5

# Iniciar o agendamento
scheduler.enter(0, 1, agendar, (intervalo,))
scheduler.run()
