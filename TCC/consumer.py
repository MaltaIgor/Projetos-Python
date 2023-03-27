import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, datetime,timedelta
import yfinance as yf
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import scipy.optimize
import mysql.connector
import pytz


conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="bolsa_valores"
)
cursor = conn.cursor()


symbol_list_ibrx = list(pd.read_csv('ibrx.csv',delimiter=";").index)
df_final = pd.DataFrame()
for ativo in symbol_list_ibrx:
    chamada_api = yf.Ticker(ativo + ".SA").history(period='36mo')
    df_hist = pd.DataFrame(chamada_api).reset_index()
    df_hist["Symbol"] = ativo
    df_hist = df_hist[["Date","Symbol","Open","High","Low","Close","Volume","Dividends"]]
    df_hist["Date"] = df_hist["Date"].dt.tz_convert(pytz.utc).dt.date
    df_hist["Date"] = df_hist["Date"].astype(str)
    df_final = pd.concat([df_hist, df_final],axis=0)

tuplas = tuple(df_final.itertuples(index=False, name=None))
query = "INSERT IGNORE INTO cotacao  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(query, tuplas)
conn.commit()
conn.close()