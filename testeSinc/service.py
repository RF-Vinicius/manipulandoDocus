import pandas as pd
import re

"""
    Lista do que significa os idCampo
    
    Revisão = 1
    Prancha = 2
    Cliente = 3
    Obra = 4
    Projeto = 5
    Disciplina = 6
    Objeto = 8
    Elemento = 9
    Assunto = 10
    Tipologia = 11
    Plano de Projeção = 12
    Localização = 13
    Local = 14
    Blocos = 15
    Fases de Construção = 16
    Não definir = 17
    Campo personalizado = 1
"""

class SincComPadrao:
    
    def __init__(self, dfDocumentos, dfPadrapoNomenclatura, dfBaseTerceira = []):
        self.__dfDocumentos = dfDocumentos
        self.__dfPadrapoNomenclatura = dfPadrapoNomenclatura
        self.__dfBaseTerceira = dfBaseTerceira
        self.__separador = dfPadrapoNomenclatura['separadores'][0].replace(",", "")
        self.__listPadroes = dfPadrapoNomenclatura['qtdSiglas'].unique()
        
    def testeDisciplinas(self):
        documentoComDisciplinaErrada = []
        documentosForaPadrao = []
        df_padrao = self.__dfPadrapoNomenclatura
        df_documentos = self.__dfDocumentos
                
        for documento in self.__dfDocumentos['NomeDocumento']:
            documentoList = re.split(f"[{self.__separador}]", documento)
            
            qtdSiglaDoc = len(documentoList) + 1 #O objeto vem sem a revisão, por isso tem + 1
            
            if qtdSiglaDoc in self.__listPadroes: #Verifica se o documento pertence a algum padrão
                posicao_siglaDisciplina = df_padrao[(df_padrao['idCampo'] == 6) & (df_padrao['qtdSiglas'] == qtdSiglaDoc)]['ordem'].unique()[0] # Adicionar dentro da validação do if, variável com base no tipo do padrão.
                
                if documentoList[posicao_siglaDisciplina - 1] in list(df_padrao[(df_padrao['qtdSiglas'] == qtdSiglaDoc) & (df_padrao['idCampo'] == 6)]['sigla']):
                    if str(df_documentos[df_documentos['NomeDocumento'] == documento]["idDisciplina"].values[0]) != df_padrao[(df_padrao['sigla'] == documentoList[posicao_siglaDisciplina - 1]) & (df_padrao['qtdSiglas'] == qtdSiglaDoc)]["preenchimento"].values[0]:
                        documentoComDisciplinaErrada.append(documento)    
                else:
                     documentosForaPadrao.append(documento)
            else:
                documentosForaPadrao.append(documento)
        
   
        return documentoComDisciplinaErrada