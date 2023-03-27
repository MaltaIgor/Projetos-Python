# IMPORTAÇÕES

from consumidor import consumer, atualizacao_carteira
from relatorio import analise_tecnica, grafico
import yfinance as yf
import finplot as fplt
import numpy as np
import pandas as pd
import mysql.connector
import datetime
import pytz
import os 
#from dotenv import load_dotenv, find_dotenv


# CONEXÃO COM BANCO DE DADOS
#load_dotenv(find_dotenv())

conn = mysql.connector.connect(
  host= "localhost", # os.getenv('host'),
  user="root", # os.getenv('user'),
  password="1234", # os.getenv('password'),
  database="bolsa_valores"
)
cursor = conn.cursor()

base = pd.read_sql('SELECT * FROM bolsa_valores.cotacao where DATE >= DATE_SUB(CURDATE(), INTERVAL 24 MONTH)', conn)

# ATUALIZAÇÃO DA BASE DE DADOS DE COTAÇÕES

consumer()



# FORMAÇÃO DA CARTEIRA FUNDAMENTALISTA
dt = datetime.today()
if datetime(dt.year,dt.month,dt.day) == datetime.date(dt.year,6,1) or (not os.path.exists('carteira.csv')):
    ativos = base['SYMBOL'].values.tolist()
    list_melhores = []
    for ativo in ativos:
        if atualizacao_carteira(ativo=ativo, base=base):
            list_melhores.append(ativo)
    pd.Series(list_melhores).to_csv('carteira.csv', index=False)



# ANALISE TÉCNICA E NOTIFICAÇÃO 
carteira = list(pd.read_csv('carteira.csv',delimiter=";"))
for ativo in carteira:
    analise = base.loc[base['SYMBOL'] == ativo]
    if analise_tecnica(ativo):
        grafico(analise)










