from bs4 import BeautifulSoup
import json
import sched
import time
import requests
from datetime import datetime

def dataCleaning(url):
    data = {}
    try:
        if not url:
            raise ValueError("A URL não pode ser vazia.")
        
        # Usar requests para obter o conteúdo da URL
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError("Falha ao obter o conteúdo da URL.")

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraindo o título do produto
        title_element = soup.find('div', class_='header-product-info--title')
        title = title_element.h2.text.strip() if title_element and title_element.h2 else 'Título não encontrado'

        # Extraindo os preços
        price_elements = soup.find('div', class_='header-product-info--price').find_all('span')
        price_usd_min = price_elements[0].text.strip() if len(price_elements) > 0 else 'Preço não encontrado'
        price_usd_max = price_elements[1].text.strip() if len(price_elements) > 1 else 'Preço não encontrado'

        # Extraindo preços em diferentes moedas
        currency_elements = soup.find('div', class_='header-product-info--currency').find_all('span')
        price_brl = currency_elements[0].text.strip() if len(currency_elements) > 0 else 'Preço não encontrado'
        price_ars = currency_elements[1].text.strip() if len(currency_elements) > 1 else 'Preço não encontrado'

        dolar_cotacao_element = soup.find('span', class_='txt-quotation')
        dolar_cotacao = dolar_cotacao_element.strong.text.strip() if dolar_cotacao_element and dolar_cotacao_element.strong else 'Cotação não encontrada'

        # Obtendo data e hora atuais
        now = datetime.now()
        data = {
            'title': title,
            'price_usd_min': price_usd_min,
            'price_usd_max': price_usd_max,
            'price_brl': price_brl,
            'price_ars': price_ars,
            'dolar_cotacao': dolar_cotacao,
            'current_date': now.strftime('%Y-%m-%d'),
            'current_time': now.strftime('%H:%M:%S')
        }

    except Exception as e:
        print(f"Erro ao analisar o HTML: {e}")
    
    return data

def agendar(intervalo):
    try:
        link = pedeLink()
        if link:
            lista_produtos = dataCleaning(link)
            if lista_produtos:
                enviar(lista_produtos)
        scheduler.enter(intervalo, 1, agendar, (intervalo,))
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")

def pedeLink():
    try:
        response = requests.get('http://node:3000/pedeLink')
        if response.status_code == 200:
            return response.text
        else:
            print(f"Erro ao obter link: Status Code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")
        return None

def enviar(lista_produtos):
    try:
        response = requests.post('http://node:3000/api/produtos', json=lista_produtos)
        if response.status_code == 200:
            print("Dados enviados com sucesso.")
        else:
            print(f"Erro ao enviar dados: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar enviar a requisição: {e}")

if __name__ == '__main__':
    print('__main__')
    intervalo = 1  # Intervalo de tempo entre execuções em segundos
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 1, agendar, (intervalo,))
    scheduler.run()
