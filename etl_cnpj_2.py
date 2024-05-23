import requests
import zipfile
import os
import glob
import shutil

#Baixando dados da receita

#funcao para baixar os arquivos da receita 
def download_cnpj(i):
    url = 'https://dadosabertos.rfb.gov.br/CNPJ/'+ i + '.zip' #criacao da url para download
    response = requests.get(url) #Busca do arquivo
    nome_arquivo_local = 'arquivo.zip' #local temporario para download
    if response.status_code == 200: #se ele achar ele faz o download
        with open(nome_arquivo_local, 'wb') as file:
            file.write(response.content)   
        with zipfile.ZipFile(nome_arquivo_local, 'r') as zip_ref: #descompacta o arquivo
            zip_ref.extractall('saida')
        arquivos = os.listdir('saida') #le o nome do arquivo
        caminho_origem = 'saida/' + arquivos[0] 
        caminho_destino = 'dados_cnpj/' + i + '.csv'
        shutil.copy(caminho_origem, caminho_destino) #Copia tirando a extensao para a csv
        shutil.rmtree('saida')  #renove a pasta temp
        os.remove('arquivo.zip') #renove o zip
        resp = 1
    else:
        resp = 0
    return resp


#download empresas
file = 'Empresas'
resp = 1
cont = 0
while resp == 1:
    aux = file + str(cont)
    resp = download_cnpj(aux)
    cont += 1

#download estabelecimentos
file = 'Estabelecimentos'
resp = 1
cont = 0
while resp == 1:
    aux = file + str(cont)
    resp = download_cnpj(aux)
    cont += 1

#Download socios
file = 'Socios'
resp = 1
cont = 0
while resp == 1:
    aux = file + str(cont)
    resp = download_cnpj(aux)
    cont += 1


#download depara
aux = ['Motivos', 'Municipios', 'Naturezas', 'Paises', 'Qualificacoes', 'Simples', 'Cnaes']
for i in aux:
    download_cnpj(i)


