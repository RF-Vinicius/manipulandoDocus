from dataclasses import replace
import os
import random
import shutil
import re

folder = "C:/Users/vini9/OneDrive/Área de Trabalho/arquivosTeste"
listaDisciplinas = ['ARQ', 'ELE', 'HID', 'EST', 'PAI', 'PIS', 'MET', 'DOC', 'PCI']
listaAreas = ['1PAV', '2PAV', '3PAV', '4PAV', '5PAV', '6PAV', '7PAV', '8PAV',
'9PAV', '10PV', 'TIPO', 'TP02', 'TP03', 'TP04', 'COBE', 'TERR', 'PLAY', 'GERR'
]

listFase = ['EX', 'LO', 'AP']

listaSeparador = ['-']

revisaoTipo = "R"

def createArquivo(folder, quantidadeDocumentos, siglaObra):

    pasta = os.listdir(folder)

    for i in range(quantidadeDocumentos):

        disciplina = random.choice(listaDisciplinas)
        numeroPlanta = str(random.randint(1000, 9000))
        #fase = random.choice(listFase)
        fase = random.choice(listFase) if round(random.random()) == 1 else random.choice(listFase).lower()
        #area = random.choice(listaAreas)
        area = random.choice(listaAreas) if round(random.random()) == 1 else random.choice(listaAreas).lower()
        revisao = revisaoTipo + '0' + "5"
        separadorDocumento = random.choice(listaSeparador)
       
        nomeDocumento = siglaObra + random.choice(listaSeparador) + disciplina + random.choice(listaSeparador) + numeroPlanta + random.choice(listaSeparador) + fase + random.choice(listaSeparador) + str(area) + random.choice(listaSeparador) + revisao
        for n in pasta:
            
            if len(n) > 4:
                extensao = n.split('.')[-1]
                caminhoAntigo = folder + '/' + n
                caminhoNovo = folder + '/' + extensao.lower() + '/' + nomeDocumento + '.' + extensao
                shutil.copy2(caminhoAntigo, caminhoNovo)


def mudarRevisao(folder, maisMenos):

    pasta = os.listdir(folder)

    for i in pasta:

        if len(i) < 5:

            pastaDocumentos = folder + '/' + i
            documentos = os.listdir(pastaDocumentos)

            for n in documentos:
                
                revisao = re.split("[-_.]", n)[-2]
                changeRevisao = int(revisao.replace(revisaoTipo, '')) + maisMenos
                newName = n.replace(revisao, revisaoTipo + "0" + str(changeRevisao))

                pastaNome = folder + '/' + i + '/' + n
                pastaNewNome = folder + '/' + i + '/' + newName
                os.rename(pastaNome, pastaNewNome)
            


def excluir_documentos(folder):

    pasta = os.listdir(folder)

    for i in pasta:
        if len(i) < 5:

            pastaDocumentos = folder + '/' + i
            documentos = os.listdir(pastaDocumentos)

            for n in documentos:
                if os.path.exists(folder + '/' + i + '/' + n): 
                    os.remove(folder + '/' + i + '/' + n)




createArquivo(folder, 5, 'CODE')
#mudarRevisao(folder, 1)
#excluir_documentos(folder)