# Tinha 5 tabelas
import requests
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/Lista_de_campe%C3%B5es_do_Campeonato_Brasileiro_de_Futebol"
cabecalhos = {"User-Agent": "Mozzila/5.0 (aula de scraping)"}
resposta = requests.get(url, headers=cabecalhos)

sopa = BeautifulSoup(resposta.text, "html.parser")

tabelas = sopa.find_all("table", {"class": "wikitable"})
tabela_campeoes = next(tabela for tabela in tabelas if "Vencedor" in tabela.find("tr").text)
linhas = []
for tr in tabela_campeoes.find_all("tr")[1:6]:
    celulas = [c.text.strip() for c in tr.find_all(["th", "td"])]
    linhas.append(celulas)


print(resposta.status_code)
print(len(resposta.text), "caracteres recebidos")

print(sopa.find("h1").text)
print(f"A página tem {len(tabelas)} tabelas do tipo wikitable")

for linha in linhas:
    print(linha)