import pandas as pd
import re
import numpy as np

df = pd.read_excel("C:/Users/vini9/OneDrive/Área de Trabalho/compararArquivo/comparar.xlsx")
#print(df["Documentos planilha"] == "741.22-AIT-EX-121-8015.00 - PJT - r00.pdf")
df.dropna()
lista_enviada = []
lista_CC = []
for nomeDoc in df['Documentos planilha']:
    doc = re.split("[-_.]", nomeDoc)
    if len(doc) > 11 and len(doc) < 15:
        for i in doc:
            if i =="741" or i == "741 22" or i == "74122 EIN" or "74122" in i:
                lista_enviada.append(doc[doc.index(i):])
                break
    elif doc[0] == "AW0553":
        for i in doc:
            if i =="741" or i == "741 22" or "74122" in i:
                lista_enviada.append(doc[doc.index(i):])
                break
    elif len(doc) >= 15:
        for i in doc:
            if i == "74122 EIN" or "74122" in i:
                lista_enviada.append(doc[doc.index(i):])
                break
    else:
        lista_enviada.append(doc)


for doc1 in df['Documentos no CC']:
    if isinstance(doc1, str):
        doc = re.split("[-_.]", doc1)
        lista_CC.append(doc)


"""for i in lista_enviada:
    if i not in lista_CC:
        #print(i, lista_enviada.index(i))
        print(df['Documentos planilha'][lista_enviada.index(i)])"""

for i in lista_CC:
    if i not in lista_enviada:
        #print(i, lista_enviada.index(i))
        print(df['Documentos no CC'][lista_CC.index(i)])