from bs4 import BeautifulSoup

html_exemplo = """
<table>
  <tr><th>Tie</th><th>Pontos</th></tr>
  <tr><td>Alfa</td><td>72</td></tr>
  <tr><td>Beta</td></tr>68</td></tr>
</table>
"""

sopa = BeautifulSoup(html_exemplo, "html.parser")
tabela = sopa.find("table")
linhas = []
for tr in tabela.find_all("tr"):
    celulas = [c.text.strip() for c in tr.find_all(["th", "td"])]
    linhas.append(celulas)
for linha in linhas:
    print(linha)