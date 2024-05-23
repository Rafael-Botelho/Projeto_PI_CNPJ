#imprta as bibliotecas
from tqdm import tqdm
import os
import datetime
import psycopg2


host = ''
database = ''
usuario = ''
senha = ''

db_connection = psycopg2.connect(host=host, database=database, user=usuario, password=senha)
cursor = db_connection.cursor()



def insert(tabela, read):
    inserir_dados = "INSERT INTO " + tabela + " VALUES "
    c = 0
    for i in tqdm(range(len(read))):
        if c <= 500:
            if c > 0:
                inserir_dados = inserir_dados + ","
            aux = read[i]
            aux = aux.replace("'", "")
            aux = aux.split('";"')
            aux[0] = aux[0].replace('"', '')
            aux[-1] = aux[-1].replace('"\n', '')
            inserir_dados = inserir_dados + "('"
            for j in range(len(aux)):
                if j < len(aux)-1:
                    inserir_dados = inserir_dados + aux[j] + "','" 
                else:
                    inserir_dados = inserir_dados + aux[j] + "')"
            c += 1
        else:
            c = 0
            try:
                cursor.execute(inserir_dados)
                db_connection.commit()
            except:
                cursor.execute('ROLLBACK')
                db_connection.commit()
                for k in range(i-500, i):
                    inserir_dados = "INSERT INTO " + tabela + " VALUES "
                    aux = read[k]
                    aux = aux.replace("'", "")
                    aux = aux.split('";"')
                    aux[0] = aux[0].replace('"', '')
                    aux[-1] = aux[-1].replace('"\n', '')
                    inserir_dados = inserir_dados + "('"
                    for j in range(len(aux)):
                        if j < len(aux)-1:
                            inserir_dados = inserir_dados + aux[j] + "','" 
                        else:
                            inserir_dados = inserir_dados + aux[j] + "')"
                    try:
                        cursor.execute(inserir_dados)
                        db_connection.commit()
                    except:
                        cursor.execute('ROLLBACK')
                        db_connection.commit()
                        print(str(k) + '   ' + inserir_dados)
                        log = open('relatorio_cnpj.log', 'a')
                        log.write(str(k) + '   ' + inserir_dados + '\n')
                        log.close()
            inserir_dados = "INSERT INTO " + tabela + " VALUES "
    cursor.execute(inserir_dados)
    db_connection.commit()

def insert2(tabela, read):
    for k in range(len(read)):
        inserir_dados = "INSERT INTO " + tabela + " VALUES "
        aux = read[k]
        aux = aux.replace("'", "")
        aux = aux.split('";"')
        aux[0] = aux[0].replace('"', '')
        aux[-1] = aux[-1].replace('"\n', '')
        inserir_dados = inserir_dados + "('"
        for j in range(len(aux)):
            if j < len(aux)-1:
                inserir_dados = inserir_dados + aux[j] + "','" 
            else:
                inserir_dados = inserir_dados + aux[j] + "')"
        try:
            cursor.execute(inserir_dados)
            db_connection.commit()
        except:
            cursor.execute('ROLLBACK')
            db_connection.commit()
            print(str(k) + '   ' + inserir_dados)
            log = open('relatorio_cnpj.log', 'a')
            log.write(str(k) + '   ' + inserir_dados + '\n')
            log.close()



data_atual = datetime.date.today()
log = open('relatorio_cnpj.log', 'a')
log.write(str(data_atual) + '\n')
log.close()



arquivos = os.listdir('dados_cnpj')

tabelas = ['Empresas', 'Estabelecimentos', 'Socios', 'Motivos', 'Municipios', 'Naturezas', 'Paises', 'Qualificacoes', 'Simples', 'Cnaes']



for t in tabelas:
    print(t)
    log = open('relatorio_cnpj.log', 'a')
    log.write(t + '\n')
    log.close()
    aux_file = []
    for i in arquivos:
        if i[0:len(t)] == t:
            aux_file.append(i)
    for i in aux_file:
        print(i)
        log = open('relatorio_cnpj.log', 'a')
        log.write(i + '\n')
        log.close()
        read = open('dados_cnpj/'+ i, 'r', encoding = "latin").readlines()
        if len(read) > 500:
            insert('cnpjs.tbl_' + t, read)
        else:
            insert2('cnpjs.tbl_' + t, read)


