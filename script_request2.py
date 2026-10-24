import requests
from bs4 import BeautifulSoup

url = "https://www.uol.com.br/esporte/ultimas-noticias/2026/10/24/rebeca-andrade-salto-mundial-ginastica.ghtm"

headers = {
    "User-Agent": "AulaManipulacaoDados/1.0 (contato: seu_email@exemplo.com)"
}

reposta = requests.get(url, headers=headers, timeout=15)

sopa =  BeautifulSoup(reposta.text, "html.parser")
links = sopa.find_all("a")

# Testes requests
print(reposta.status_code)
print(reposta.text[:300])

# Testes beautifulsoup
titulo = sopa.find("h1")
print(titulo.text)

primeiro_paragrafo = sopa.find("p")
print(primeiro_paragrafo.text[:200])

print(f"A página tem {len(links)} links")

for link in links[:5]:
    print(link.text.strip(), "->", link.get("href"))
    