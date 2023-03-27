def consumer():
    x = pd.read_sql("SELECT DISTINCT SYMBOL FROM cotacao", conn)
    symbol_list_ibrx = list(pd.read_csv('ibrx.csv',delimiter=";").index)
    symbol_list_ibrx = symbol_list_ibrx + x['SYMBOL'].values.tolist()
    symbol_list_ibrx = set(symbol_list_ibrx)
    symbol_list_ibrx
    df_final = pd.DataFrame()
    for ativo in symbol_list_ibrx:
        if(ativo in x):
            chamada_api = yf.Ticker("PETR4.SA").history(period='1wk')
        else:    
            chamada_api = yf.Ticker("PETR4.SA").history(start = date(2020, 3, 23))
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



def analise_tecnica(ativo):





def carteira():
