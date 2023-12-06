#pip install mysql-connector-python==8.0.13
import mysql.connector
from mysql.connector import constants
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

try:
    # Estabelecer a conexão segura
    conexao = mysql.connector.connect(**ssl_config)

    # Resto do código para consulta e manipulação de dados...
    cursor = conexao.cursor()

    # Executar uma consulta SELECT
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
            pn.idObra = {1310}
    """
    cursor.execute(consulta)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

    x = pd.DataFrame(resultados, columns=['sigla', 'preenchimento', 'separadores', 'qtdSiglas', 'ordem', 'idCampo'])

except mysql.connector.Error as error:
    print(f"Erro ao conectar-se ao banco de dados MySQL: {error}")
    
print(x)