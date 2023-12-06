import requests
import pandas as pd

list_id = "187019727"
url = "http://teste.construcode.com.br/API/GetProjetosByFilter/"

query = {
"APIKey": "40B8D99A-FBA8-4755-BF27-0C454F3F27C8",
"deviceID": "399e840d28361946",
"app": "3.2.1.76",
"accessToken": "2969d025-df54-4b96-ae54-2b2100e053b0",
"idObra": "1310",
"VAPP": 0
}


response = requests.get(url, params=query)
data = response.json()
listaDocumentosObra = []

for i in data["Result"]["Projetos"]:
    listaDocumentosObra.append(
        [
            i['Nome'],
            i['Tipo'],
            i['IDTipo'],
            i['Fase'],
            i['Areas']
        ]
    )

df_documentos = pd.DataFrame(listaDocumentosObra, columns=['NomeDocumento', 'SiglaDisciplina', 'idDisciplina', 'idFase', 'Areas'])