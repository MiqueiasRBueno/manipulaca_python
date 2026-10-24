import requests
url = "https://pt.wikipedia.org/wiki/Python"

headers = {
    "User-Agent": "AulaManipulacaoDados/1.0 (contato: seu_email@exemplo.com)"
}

reposta = requests.get(url, headers=headers, timeout=15)

print(reposta.status_code)
print(reposta.text[:3000])