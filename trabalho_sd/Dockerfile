# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Instale curl e outras dependências necessárias
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean

# RUN pip freeze > requirements.txt

# # Instalar o BeautifulSoup
# RUN pip install -r requirements.txt

# # Adicione seu script Python e de bash ao container
# COPY scraper.sh /usr/src/app/scraper.sh
# COPY parser.py /usr/src/app/parser.py

# # Defina o diretório de trabalho
# WORKDIR /usr/src/app

# # Dê permissão de execução ao script bash
# RUN chmod +x scraper.sh

# # Comando para rodar o script bash
# CMD ["./scraper.sh"]


docker cp trabalho_sd/getPage.sh containerzin:/usr/src/app/scraper.sh
