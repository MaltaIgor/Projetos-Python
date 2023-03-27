import yfinance as yf
import finplot as fplt
import numpy as np
import pandas as pd
import mysql.connector
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="bolsa_valores"
)
cursor = conn.cursor()

chamada_api = pd.read_sql('SELECT * FROM cotacao', conn)
chamada_api = chamada_api.loc[chamada_api['SYMBOL'] == 'PETR4']


def plot_accumulation_distribution(df, ax):
    ad = (2*df.CLOSE-df.HIGH-df.LOW) * df.VOLUME / (df.HIGH - df.LOW)
    ad.cumsum().ffill().plot(ax=ax, legend='Accum/Dist', color='#f00000')


def plot_bollinger_bands(df, ax):
    mean = df.CLOSE.rolling(20).mean()
    stddev = df.CLOSE.rolling(20).std()
    df['boll_hi'] = mean + 2.5*stddev
    df['boll_lo'] = mean - 2.5*stddev
    p0 = df.boll_hi.plot(ax=ax, color='#808080', legend='BB')
    p1 = df.boll_lo.plot(ax=ax, color='#808080')
    fplt.fill_between(p0, p1, color='#1A1C1D')


def plot_ema(df, ax):
    df.CLOSE.ewm(span=9).mean().plot(ax=ax, legend='EMA',color = '#eef')


def plot_rsi(df, ax):
    diff = df.CLOSE.diff().values
    gains = diff
    losses = -diff
    with np.errstate(invalid='ignore'):
        gains[(gains<0)|np.isnan(gains)] = 0.0
        losses[(losses<=0)|np.isnan(losses)] = 1e-10 
    n = 14
    m = (n-1) / n
    ni = 1 / n
    g = gains[n] = np.nanmean(gains[:n])
    l = losses[n] = np.nanmean(losses[:n])
    gains[:n] = losses[:n] = np.nan
    for i,v in enumerate(gains[n:],n):
        g = gains[i] = ni*v + m*g
    for i,v in enumerate(losses[n:],n):
        l = losses[i] = ni*v + m*l
    rs = gains / losses
    df['rsi'] = 100 - (100/(1+rs))
    df.rsi.plot(ax=ax, legend='RSI')
    fplt.set_y_range(-20, 120, ax=ax)
    fplt.add_band(3, 97, ax=ax, color='#1A1C1D')


def plot_moving_avg(df, ax):
    ma20 = df.CLOSE.rolling(20).mean()
    ma50 = df.CLOSE.rolling(50).mean()
    fplt.plot(ma20, legend = "MA-20", ax=ax)
    fplt.plot(ma50, legend = "MA-50", ax=ax)


def plot_candles(df, ax):
    candles = df[['OPEN', 'CLOSE', 'HIGH', 'LOW']]
    daily_plot = fplt.candlestick_ochl(candles, candle_width=1)
    daily_plot.colors.update(dict(bull_body='#bfb', bull_shadow='#ada', bear_body='#fbc', bear_shadow='#dab'))


def plot_volume(df, ax):
    df_renko = chamada_api.reset_index()
    df_renko["DATE"] = pd.to_datetime(df_renko['DATE'])
    fplt.volume_ocv(df_renko[['DATE','OPEN','CLOSE','VOLUME']], ax=ax)
    fplt.plot(df_renko.VOLUME.ewm(span=24).mean(), ax=ax, color='#eef', legend='Volume')

def grafico(df):
    ax,ax2,ax3,ax4 = fplt.create_plot(title='Gráfico', rows = 4, maximize=True)
    b = fplt.background = fplt.odd_plot_background = '#010101'
    w = fplt.foreground = '#eef'
    fplt.cross_hair_color = w+'a'

    plot_candles(chamada_api, ax)
    plot_volume(chamada_api, ax2)
    plot_bollinger_bands(chamada_api, ax)
    plot_ema(chamada_api, ax)
    plot_accumulation_distribution(chamada_api, ax3)
    plot_rsi(chamada_api, ax4)
    plot_moving_avg(chamada_api, ax)
    fplt.show()

