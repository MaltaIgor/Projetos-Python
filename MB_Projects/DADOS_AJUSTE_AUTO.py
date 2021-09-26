#CONEXAO BD, PYTHON

import pyodbc
import pandas as pd
#import numpy as np
#import cvxpy as cp 
#import scipy as sc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SQL...;'
                      'Database=DATABASE;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

CUSTODIA = pd.read_sql_query("SELECT TECE, VLR, SUM(VALOR_TOTAL) AS SALDO FROM GESTAO WHERE DESCRICAO != 'PROG' AND TIPO = 'Família' GROUP BY TECE, VLR ORDER BY TECE, VLR DESC",conn)
B_RESTRICOES = pd.read_sql_query('SELECT * FROM BASE_RESTRI',conn)
B_OBJETIVO = pd.read_sql_query('SELECT * FROM PROP_CEDU',conn)


TECES = (B_RESTRICOES.COD_CEN.unique())
for i in TECES:
    print(CUSTODIA[CUSTODIA.TECE == i])
    print(B_OBJETIVO[B_OBJETIVO.TECE == i])
    PERFIS = (B_RESTRICOES.PERFIL.unique())
    for n in PERFIS:
        print(B_RESTRICOES[(B_RESTRICOES.TECE == i) & (B_RESTRICOES.PERFIL == n)])



conn.close()


#PROJETO FARIA CALCULO DE OTIMIZAÇÃO POR MINIMIZAÇÃO, PORÉM PARTE DO CODIGO CENSURADA.

#TABELA PARA INSERÇÃO DOS RESULTADOS ( já com código python)
df.to_sql(
name = 'TI_AJUSTE_AUTO',
con = conn,
index = False,
if_exists = 'append'
)
