import psycopg2

# db_connection = psycopg2.connect(host='192.168.10.140', database='pitlake', user='rafael_pit', password='Pit@2023#')

host = ''
database = ''
usuario = ''
senha = ''

db_connection = psycopg2.connect(host=host, database=database, user=usuario, password=senha)

cursor = db_connection.cursor()


query = """drop table cnpjs.tbl_cnaes"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_empresas"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_estabelecimentos"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_motivos"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_municipios"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_naturezas"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_paises"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_qualificacoes"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_socios"""
cursor.execute(query)
db_connection.commit()

query = """drop table cnpjs.tbl_simples"""
cursor.execute(query)
db_connection.commit()


#tabela empresa
query = """CREATE TABLE cnpjs.tbl_EMPRESAS (
nu_cnpj VARCHAR(10) NOT NULL,
nm_empresa VARCHAR(200),
CD_NATUREZA bigint,
cd_QUALIFICACAO bigint,
vl_CAPITAL VARCHAR(20),
cd_PORTE VARCHAR(2),
ds_ENTE_FEDERATIVO_RESPONSAVEL VARCHAR(200))"""
cursor.execute(query)
db_connection.commit()


#tabela estabelecimento
query = """CREATE TABLE cnpjs.tbl_ESTABELECIMENTOS (
nu_cnpj VARCHAR(10) NOT NULL,
nu_CNPJ_ORDEM VARCHAR(10),
nu_CNPJ_DV VARCHAR(10),
ID_MATRIZ_FILIAL VARCHAR(1),
NM_FANTASIA VARCHAR(200),
ST_CADASTRAL VARCHAR(2), 
DT_SITUACAO_CADASTRAL VARCHAR(8),
MT_SITUACAO_CADASTRAL VARCHAR(50),
NM_CIDADE_EXTERIOR VARCHAR(100),
cd_PAIS VARCHAR(50),
DT_INICIO_ATIVIDADE VARCHAR(8),
nu_CNAE_PRINCIPAL bigint,
nu_CNAE_SECUNDARIO text,
TP_LOGRADOURO VARCHAR(20),
ds_LOGRADOURO VARCHAR(200),
nu_logradouro VARCHAR(10),
ds_COMPLEMENTO VARCHAR(200),
ds_BAIRRO VARCHAR(200),
NU_CEP VARCHAR(10),
SG_UF VARCHAR(10),
CD_MUNICIPIO VARCHAR(10),
nu_DDD1 VARCHAR (10),
nu_TELEFONE1 VARCHAR(10),
nu_DDD2 VARCHAR (10),
nu_TELEFONE2 VARCHAR(10),
nu_DDD_FAX VARCHAR (10),
nu_FAX VARCHAR(10),
ds_EMAIL VARCHAR(100),
ST_ESPECIAL VARCHAR(20),
DT_SITUACAO_ESPECIAL VARCHAR(8))"""
cursor.execute(query)
db_connection.commit()


#tabela simples
query = """CREATE TABLE cnpjs.tbl_SIMPLES (
nu_CNPJ VARCHAR(10),
OP_SIMPLES VARCHAR(10),
DT_OPCAO_SIMPLES VARCHAR(8),
DT_EXCLUSAO_SIMPLES VARCHAR(8),
OP_MEI VARCHAR(10),
DT_OPCAO_MEI VARCHAR(8),
DT_EXCLUSAO_MEI VARCHAR(8))"""
cursor.execute(query)
db_connection.commit()



#tabela socios
query = """CREATE TABLE cnpjs.tbl_SOCIOS (
nu_CNPJ VARCHAR(10),
ID_SOCIO VARCHAR(200),
NM_SOCIO VARCHAR(200),
nu_CNPJ_CPF_SOCIO VARCHAR(20),
QL_SOCIO VARCHAR(20),
DT_ENTRADA_SOCIO VARCHAR(8),
cd_PAIS VARCHAR(200),
ds_REPRESENTANTE_LEGAL VARCHAR(20),
NM_REPRESENTANTE VARCHAR(200),
QL_REPRESENTENTE VARCHAR(20),
FX_ETARIA VARCHAR(20))"""
cursor.execute(query)
db_connection.commit()



#tabela paises
query = """CREATE TABLE cnpjs.tbl_PAISES (
cd_pais bigint,
ds_pais VARCHAR(200))"""
cursor.execute(query)
db_connection.commit()



#tabela municipio
query = """CREATE TABLE cnpjs.tbl_MUNICIPIOS (
cd_municipio bigint,
ds_municipio VARCHAR(200))"""
cursor.execute(query)
db_connection.commit()



#tabela qualificacao
query = """CREATE TABLE cnpjs.tbl_QUALIFICACOES (
cd_qualificacao bigint,
ds_qualificacao VARCHAR(200))"""
cursor.execute(query)
db_connection.commit()



#tabela natureza
query = """CREATE TABLE cnpjs.tbl_NATUREZAS (
CD_NATUREZA bigint,
DS_NATUREZA VARCHAR(200))"""
cursor.execute(query)
db_connection.commit()



#tabela cnaes
query = """CREATE TABLE cnpjs.tbl_CNAES (
cd_cnae bigint,
ds_cnae VARCHAR(200))"""
cursor.execute(query)
db_connection.commit()


#tabela motivos
query = """CREATE TABLE cnpjs.tbl_MOTIVOS (
cd_motivo bigint,
ds_motivo VARCHAR(200))"""
cursor.execute(query)
db_connection.commit()
