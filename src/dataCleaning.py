from bs4 import BeautifulSoup

# Nome do arquivo HTML
nome_arquivo = "src/pageCompras.html"

# Ler o conteúdo do arquivo HTML
with open(nome_arquivo, 'r', encoding='utf-8') as file:
    html = file.read()

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todos os blocos de produtos
produtos = soup.find_all('div', class_='promocao-produtos-item')

# Lista para armazenar os objetos de produtos
lista_produtos = []

# Iterar sobre cada produto e extrair as informações
for produto in produtos:
    # Extrair o nome do produto
    produto_nome = produto.find('div', class_='promocao-item-nome').get_text(strip=True)
    
    # Extrair o preço do produto (em dólares)
    produto_preco = produto.find('div', class_='promocao-item-preco-oferta').find('strong').get_text(strip=True)
    
    # Extrair o nome da loja
    loja_nome = produto.find('div', class_='promocao-item-preco-oferta promocao-item-border flex column').find('img', class_='lozad')['alt']
    
    # Criar um dicionário para o produto e adicionar à lista
    produto_obj = {
        "nome": produto_nome,
        "preco": produto_preco,
        "loja": loja_nome
    }
    lista_produtos.append(produto_obj)

# Exibir a lista de produtos
for produto in lista_produtos:
    print(produto)