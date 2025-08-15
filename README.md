# 📰 Extrator de Notícias com Interface HTML

# 📝 Descrição
Este é um script em Python que utiliza a técnica de web scraping para extrair as manchetes de notícias em tempo real da página inicial do portal G1.

Diferente de uma simples saída no terminal, este projeto gera uma página HTML limpa e estilizada com as notícias encontradas e a abre automaticamente no seu navegador padrão. O objetivo é demonstrar não apenas a extração de dados da web, mas também a capacidade de apresentar esses dados de forma amigável e visualmente agradável.

 Funcionalidades
- Conecta-se à página inicial do G1.
  
-  Analisa o HTML da página para encontrar os títulos e links das notícias principais.
  
-  Gera um arquivo noticias.html com as manchetes formatadas em uma lista.
  
- Os links na página são clicáveis e levam diretamente para a notícia no site do G1.
  
- Abre automaticamente a página gerada no navegador para visualização imediata.
- obs: Caso não abra, selecione o arquivo HTML e abra com o navegador de sua preferência.


# Tecnologias Utilizadas
- Python 3

- Requests: Para realizar as requisições HTTP.

- BeautifulSoup4: Para analisar o documento HTML.

- Webbrowser & OS: Módulos padrão do Python para abrir o arquivo HTML no navegador.

# Como Executar o Projeto
Siga os passos abaixo para executar o projeto localmente.

-  Clone o repositório (ou baixe os arquivos):
  
-  git clone https://github.com/Jefferson-Santana-Santos/extrator-de-noticias-python.git
  
-  Navegue até o diretório onde você colocou o projeto:

-  use o comando para executar no prompt :
  
-  cd SEU-REPOSITORIO (onde salvou o código do projeto. ex:  cd \download)
  
-  Instale as dependências necessárias:
  
-  pip install requests beautifulsoup4
  
#  Execute o script:
  
-  python extrator_noticias.py
  
-  Após a execução, o script criará o arquivo noticias.html e o abrirá no seu navegador.

# 📋 Resultado Esperado
Ao executar o script, uma nova aba será aberta no seu navegador, exibindo uma página parecida com esta:

<img width="961" height="242" alt="image" src="https://github.com/user-attachments/assets/cb37a8a8-42fd-4bb1-9851-ea308674c08b" />


A página terá um design moderno, com as manchetes listadas e prontas para serem clicadas.
