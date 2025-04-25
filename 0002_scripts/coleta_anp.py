import requests

# URL do arquivo CSV do 2º semestre de 2024
url = "https://dados.anp.gov.br/dataset/serie-historica-de-precos-de-combustiveis/resource/9c51a5e0-f4fa-4821-9e4d-9df90e5c28ba/download/preco-medio-combustiveis-2sem-2024.csv"


# Baixar o arquivo
response = requests.get(url)
response.raise_for_status()  # Verifica se o download foi bem-sucedido