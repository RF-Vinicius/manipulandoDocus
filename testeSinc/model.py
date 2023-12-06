#pip install mysql-connector-python==8.0.13
import mysql.connector
import pandas as pd
import requests

# Configuração para a conexão com SSL/TLS
ssl_config = {
    'user': 'dev_user',
    'password': '123456aaff',
    'host': 'banco01.mysql.database.azure.com',
    'port': '3306',
    'database': 'construcode_dump',
}

class ConectarBanco:
    
    def __init__(self, idObra, ssl_config):
        self.__idObra = idObra
        self.__ssl_config = ssl_config
    
    @property
    def idObra(self):
        return self.__idObra
    @idObra.setter
    def idObra(self, idObra):
        self.__idObra = idObra

    @property
    def ssl_config(self):
        return self.__ssl_config
    @ssl_config.setter
    def ssl_config(self, ssl_config):
        self.__ssl_config = ssl_config
    
    
    def listarPadrao(self):
        try:
            # Estabelecer a conexão segura
            conexao = mysql.connector.connect(**self.__ssl_config)

            # Resto do código para consulta e manipulação de dados
            cursor = conexao.cursor()

            # Executar uma consulta SELECT
            consulta = f"""
                select
                    pncr.origem, pncr.destino, pn.separador, pn.quantidadeSiglas, pnc.ordem, pnc.idCampo
                from
                    padrao_nomenclatura as pn
                inner join
                    padrao_nomenclatura_campo as pnc on (pn.id = pnc.idPadrao)
                inner join
                    padrao_nomenclatura_campo_referencia as pncr on (pnc.id = pncr.idPadraoCampo)
                inner join 
                    tipo as tp on (pncr.destino = tp.id)
                where
                    pn.idObra = {self.__idObra}
            """
            cursor.execute(consulta)

            # Recuperar os resultados da consulta
            resultados = cursor.fetchall()

            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()
            
            return pd.DataFrame(resultados, columns=['sigla', 'preenchimento', 'separadores', 'qtdSiglas', 'ordem', 'idCampo'])

        except mysql.connector.Error as error:
            print(f"Erro ao conectar-se ao banco de dados MySQL: {error}")
    
    def dadosAcessoApi():
        pass #Falta implementar aq
    
class ApiCC:
    
    def __init__(self, APIKey, deviceID, accessToken, idObra):
        self.__APIKey = APIKey
        self.__deviceID = deviceID
        self.__app = "3.2.1.76"
        self.__accessToken = accessToken
        self.__idObra = idObra
        self.__VAPP = 0   
    
    
    def requestDocumentos(self):
        list_id = "187019727"
        url = "http://teste.construcode.com.br/API/GetProjetosByFilter/"

        query = {
        "APIKey": f"{self.__APIKey}",
        "deviceID": f"{self.__deviceID}",
        "app": f"{self.__app}",
        "accessToken": f"{self.__accessToken}",
        "idObra": f"{self.__idObra}",
        "VAPP": f"{self.__VAPP}"
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

        return pd.DataFrame(listaDocumentosObra, columns=['NomeDocumento', 'SiglaDisciplina', 'idDisciplina', 'idFase', 'Areas'])
    