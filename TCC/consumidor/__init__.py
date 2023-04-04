def consumer():
    x = pd.read_sql("SELECT DISTINCT SYMBOL FROM cotacao", conn)
    symbol_list_ibrx = list(pd.read_csv('ibrx.csv',delimiter=";").index)
    symbol_list_ibrx = symbol_list_ibrx + x['SYMBOL'].values.tolist()
    symbol_list_ibrx = set(symbol_list_ibrx)
    symbol_list_ibrx
    df_final = pd.DataFrame()
    for ativo in symbol_list_ibrx:
        try:
            if(ativo in x):
                chamada_api = yf.Ticker(ativo + ".SA").history(period='1mo')
            else: 

                chamada_api = yf.Ticker(ativo + ".SA").history(period='1mo')
            df_hist = pd.DataFrame(chamada_api).reset_index()
            df_hist["Symbol"] = ativo
            df_hist = df_hist[["Date","Symbol","Open","High","Low","Close","Volume","Dividends"]]
            df_hist["Date"] = df_hist["Date"].dt.tz_convert(pytz.utc).dt.date
            df_hist["Date"] = df_hist["Date"].astype(str)
            df_final = pd.concat([df_hist, df_final],axis=0)
            df_final = df_final.dropna(subset=["Date","Symbol","Open","High","Low","Close","Volume","Dividends"])
        except:
            pass
    tuplas = tuple(df_final.itertuples(index=False, name=None))
    query = "INSERT IGNORE INTO cotacao  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, tuplas)
    conn.commit()




def atualizacao_carteira(ativo, base):
    soma_fundamentos = 0
    dividend_yield = 0
    chamada_api = base.loc[base['SYMBOL'] == ativo]
    hist_precos = chamada_api['CLOSE']
    hist_dividendos = chamada_api['DIVIDENDS']
    hist_dividendos_ultimo_ano = hist_dividendos.loc[datetime((datetime.today().year-2),1,1):datetime((datetime.today().year-1),12,31)]
    hist_dividendos_ultimo_ano
        

    dividend_yield = (hist_dividendos_ultimo_ano.sum()/2)/hist_precos[-1] if hist_precos[-1] > 0 else 0
    if dividend_yield > 0.03:

        balanco_anual = yf.Ticker(ativo +'.SA').balance_sheet
        balanco_trimestral = yf.Ticker(ativo +'.SA').quarterly_balance_sheet
        dre_anual = yf.Ticker(ativo +'.SA').financials
        dfc_anual = yf.Ticker(ativo +'.SA').cashflow
        dre_trimestral = yf.Ticker(ativo +'.SA').quarterly_financials
        dfc_trimestral = yf.Ticker(ativo +'.SA').quarterly_cashflow
        
        if dre_anual.keys()[0].year >= 0:
            balanco = balanco_anual
            dre = dre_anual
            dfc = dfc_anual
            variacao_receita = int(dre.loc['Total Revenue'][0] > dre.loc['Total Revenue'][1])
            variacao_ebit = int(dre.loc['Ebit'][0] > dre.loc['Ebit'][1])
            variacao_caixa = int(dfc.loc['Change In Cash'][0] > dfc.loc['Change In Cash'][1])
            variacao_divida = int(balanco.loc['Total Current Liabilities'][0] < balanco.loc['Total Current Liabilities'][1])
            
            soma_fundamentos = variacao_caixa + variacao_ebit + variacao_receita + variacao_divida
            if soma_fundamentos > 2:
                return True
            else:
                return False