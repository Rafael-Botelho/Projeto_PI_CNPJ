import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import subprocess

print('Execultadando')
read = open('log_cnpjs_download.log', 'r').readlines()
ult_alt_dl = read[-1].split()[2]
options = webdriver.ChromeOptions()
options.add_argument('--headless') #execulta em segundo plano
url = 'https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj'
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(10)
conteudo_html = driver.page_source
driver.quit()
for i in range(len(conteudo_html)):
    if conteudo_html[i:i+18] == 'Última alteração: ':
        ult_alt_site = conteudo_html[i + 18: i + 28]

data_atual = datetime.now()
data_formatada = data_atual.strftime('%d/%m/%Y')
hora_formatada = data_atual.strftime('%H:%M:%S')
if not ult_alt_dl == ult_alt_site:
    print('Atualizando')
    saida = open('log_cnpjs_download.log', 'a')
    saida.write(data_formatada + '\t' + hora_formatada + '\t' + ult_alt_site + '\t' + '1' + '\n')
    saida.close()
    saida = open('log_cnpj.txt', 'a')
    saida.write('Atualizando banco de dados' + '\t' + data_formatada + '\t' + hora_formatada + '\n')
    subprocess.run(["python3", "etl_cnpj_2.py"])
    hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    saida.write('Extracao completa' + '\t' + hora_atual + '\n')
    subprocess.run(["python3", "etl_cnpj_3.py"])
    hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    saida.write('Tabelas criadas' + '\t' + hora_atual + '\n')
    subprocess.run(["python3", "etl_cnpj_4.py"])
    hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    saida.write('Povoamento das tabelas completo' + '\t' + hora_atual + '\n')
    saida.close()
else:
    saida = open('log_cnpjs_download.log', 'a')
    saida.write(data_formatada + '\t' + hora_formatada + '\t' + ult_alt_site + '\t' + '0' + '\n')
    saida.close()
