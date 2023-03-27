# IMPORTAÇÕES

from consumidor import consumer, analise_tecnica, atualizacao_carteira
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

base = pd.read_sql('SELECT * FROM cotacao', conn)

# ATUALIZAÇÃO DA BASE DE DADOS DE COTAÇÕES

consumer()



# FORMAÇÃO DA CARTEIRA FUNDAMENTALISTA
dt = datetime.today()
if dt == datetime.date(dt.year,6,1) or (not os.path.exists('carteira.csv')):
    ativos = base['SYMBOL'].values.tolist()
    list_melhores = []
    for ativo in ativos:
        if atualizacao_carteira():
            list_melhores.append(ativo)
    pd.Series(list_melhores).to_csv('carteira.csv', index=False)



# ANALISE TÉCNICA E NOTIFICAÇÃO 
carteira = list(pd.read_csv('carteira.csv',delimiter=";"))
for ativo in carteira:
    analise = base.loc[base['SYMBOL'] == ativo]
    if analise_tecnica(ativo):
        grafico(analise)










