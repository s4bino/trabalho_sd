import subprocess

# Definindo a URL e o nome do arquivo de saída
url = "https://www.amazon.com.br/Viol%C3%A3o-Strinberg-Sd200c-El%C3%A9trico-Tabaco/dp/B07VLJKRLX/ref=sr_1_13?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3NIO4ALR5XLN1&dib=eyJ2IjoiMSJ9.mUIS7BZ4Bf5rZKesecoWE2TC8VzUSYtUk0dvHITOiPPfLYgAWNu7t-EyifWmj4i1pinpu19cE4b4xZwu_H-5DvFLIMcu3oNS9acJwdScGvDTRIhpsTSjuGbGzHVmZegLVDw2emoeWyuVnQEusClLR6emaQW6VyagGDOQ6_7qgHcBl6ivEDw0RwqCGyEUwuDnMQ-u7HZzUadrALwqwA29J9rWx1gvlN3SjOwBZAKliLaKt5JXVn6hbpLD_CWdIZhaJpDjwmdFUt34o-6hTxoKC_Cgpx1bknzCgYHSPbiI0k4.K2w1nd1nLsmYNyzt4RM9SpZtBv9jbIh6LAXKnXFxWhM&dib_tag=se&keywords=violao&qid=1723300079&sprefix=violao%2Caps%2C210&sr=8-13&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"
output_file = "page.html"

# Comando curl para baixar a página
command = ["curl", "-sL", url, "-o", output_file]

# Executando o comando
subprocess.run(command, check=True)
