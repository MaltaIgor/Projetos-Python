# IMPORTAÇÕES

from consumidor import consumer, analise_tecnica
from relatorio import grafico
import yfinance as yf
import finplot as fplt
import numpy as np
import pandas as pd
import mysql.connector
import datetime
import os 
from dotenv import load_dotenv, find_dotenv


# CONEXÃO COM BANCO DE DADOS
load_dotenv(find_dotenv())

conn = mysql.connector.connect(
  host= os.getenv('host'),
  user=os.getenv('user'),
  password=os.getenv('password'),
  database="bolsa_valores"
)
cursor = conn.cursor()



# ATUALIZAÇÃO DA BASE DE DADOS DE COTAÇÕES

consumer()



# FORMAÇÃO DA CARTEIRA FUNDAMENTALISTA E 
dt = datetime.today()
if dt == datetime.date(dt.year,6,1):
    #atualização_carteira()
    1



# ANALISE TÉCNICA E NOTIFICAÇÃO 
carteira = list(pd.read_csv('carteira.csv',delimiter=";"))
base = pd.read_sql('SELECT * FROM cotacao', conn)
for ativo in carteira:
    analise = base.loc[base['SYMBOL'] == ativo]
    if analise_tecnica(ativo):
        grafico(analise)










