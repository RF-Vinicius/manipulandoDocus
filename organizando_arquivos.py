import os

local = 'C:/Users/vini9/OneDrive/Área de Trabalho/Residêncial ConstruCode'

def haveFolder(name, local):
    
    have = False
    teste = os.listdir(local)

    for i in teste:

        if i.lower() == name.lower():
            have = True
    
    return have

def createFolder(nome, local):

    teste = haveFolder(nome, local)

    if not teste:
        new_folder = local + '/' + nome
        os.mkdir(new_folder)


def organizarDocumentos(local):
    lista_arquivos = os.listdir(local)

    for i in lista_arquivos:

        x = i.split('.')

        if len(x) >= 2:
            extensao = x[-1]
            nome_anterior = local + '/' + i

            if not haveFolder(extensao, local):
                createFolder(extensao, local)
                alterar_arquivo = local + '/' + extensao + '/' + i
                os.rename(nome_anterior, alterar_arquivo)
            else:
                 alterar_arquivo = local + '/' + extensao + '/' + i
                 os.rename(nome_anterior, alterar_arquivo)


organizarDocumentos(local)