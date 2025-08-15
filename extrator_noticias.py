import requests
from bs4 import BeautifulSoup

# URL e headers para simular um navegador
url = 'https://g1.globo.com/'
headers = {'User-Agent': 'Mozilla/5.0'}

# Faz a requisição e obtém o conteúdo HTML
response = requests.get(url, headers=headers)

# Verifica se a conexão foi bem-sucedida
if response.status_code == 200:
    # Usa o BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra todas as tags <a> com a classe 'feed-post-link'
    # Esta é a classe que o G1 usa para suas manchetes principais
    manchetes = soup.find_all('a', class_='feed-post-link')

    print("--- MANCHETES DO G1 ---")
    # Itera sobre a lista de manchetes encontradas e imprime o texto de cada uma
    for i, manchete in enumerate(manchetes, 1):
        print(f"{i}: {manchete.get_text(strip=True)}")
    print("-----------------------")

else:
    print(f"Falha na conexão. Código: {response.status_code}")