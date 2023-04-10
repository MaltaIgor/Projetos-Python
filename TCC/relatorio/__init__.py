import yfinance as yf
import finplot as fplt
import numpy as np
import pandas as pd
import mysql.connector
import datetime
import pytz
import os 
import telebot

conn = mysql.connector.connect(
  host= "localhost", # os.getenv('host'),
  user="root", # os.getenv('user'),
  password="1234", # os.getenv('password'),
  database="bolsa_valores"
)
cursor = conn.cursor()
def plot_accumulation_distribution(df, ax):
    df['ad'].plot(ax=ax, legend='Accum/Dist', color='#f00000')


def plot_bollinger_bands(df, ax):
    p0 = df.boll_hi.plot(ax=ax, color='#808080', legend='BB')
    p1 = df.boll_lo.plot(ax=ax, color='#808080')
    fplt.fill_between(p0, p1, color='#1A1C1D')


def plot_ema(df, ax):
    df.CLOSE.ewm(span=9).mean().plot(ax=ax, legend='EMA',color = '#eef')


def plot_rsi(df, ax):
    df.rsi.plot(ax=ax, legend='RSI')
    fplt.set_y_range(-20, 120, ax=ax)
    fplt.add_band(3, 97, ax=ax, color='#1A1C1D')


def plot_moving_avg(df, ax):
    fplt.plot(df.ma20, legend = "MA-20", ax=ax)
    fplt.plot(df.ma50, legend = "MA-50", ax=ax)


def plot_candles(df, ax):
    candles = df[['OPEN', 'CLOSE', 'HIGH', 'LOW']]
    daily_plot = fplt.candlestick_ochl(candles, candle_width=1)
    daily_plot.colors.update(dict(bull_body='#bfb', bull_shadow='#ada', bear_body='#fbc', bear_shadow='#dab'))


def plot_volume(df, ax):
    df_renko = df.reset_index()
    df_renko["DATE"] = pd.to_datetime(df_renko['DATE'])
    fplt.volume_ocv(df_renko[['DATE','OPEN','CLOSE','VOLUME']], ax=ax)
    fplt.plot(df_renko.VOLUME.ewm(span=24).mean(), ax=ax, color='#eef', legend='Volume')

def grafico(df):
    
    b = fplt.background = fplt.odd_plot_background = '#010101'
    w = fplt.foreground = '#eef'
    fplt.cross_hair_color = w+'a'
    ax,ax2,ax3,ax4 = fplt.create_plot(title='Gráfico', rows = 4, maximize=True)

    plot_candles(df, ax)
    plot_volume(df, ax2)
    plot_bollinger_bands(df, ax)
    plot_ema(df, ax)
    plot_accumulation_distribution(df, ax3)
    plot_rsi(df, ax4)
    plot_moving_avg(df, ax)
    def save():
        fplt.screenshot(open('grafico.png', 'wb'))
        fplt.close()
    fplt.timer_callback(save, 0.5, single_shot=True) # wait some until we're rendered

    fplt.show()






def analise_tecnica(chamada_api):
    #media de volume
    chamada_api['m_vol'] = chamada_api.VOLUME.ewm(span=24).mean()

    #medias móveis
    chamada_api['ma20'] = chamada_api.CLOSE.rolling(20).mean()
    chamada_api['ma50'] = chamada_api.CLOSE.rolling(50).mean()

    #bollinger bands
    mean = chamada_api.CLOSE.rolling(20).mean()
    stddev = chamada_api.CLOSE.rolling(20).std()
    chamada_api['boll_hi'] = mean + 2.5*stddev
    chamada_api['boll_lo'] = mean - 2.5*stddev

    #acumulação e distribuição
    ad = (2*chamada_api.CLOSE-chamada_api.HIGH-chamada_api.LOW) * chamada_api.VOLUME / (chamada_api.HIGH - chamada_api.LOW)
    chamada_api['ad'] = ad.cumsum().ffill()
    chamada_api['ad20'] = chamada_api.ad.rolling(20).mean()
    chamada_api['ad50'] = chamada_api.ad.rolling(50).mean()
    #indice relativo
    diff = chamada_api.CLOSE.diff().values
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
    chamada_api['rsi'] = 100 - (100/(1+rs))

    analise = chamada_api.loc[pd.to_datetime(chamada_api['DATE']) == pd.to_datetime(chamada_api['DATE']).nlargest(1).iloc[0]]

    rsi = analise['rsi'] < 30
    ad = analise['ad20'] > analise['ad50']
    ma = analise['ma20'] > analise['ma50']
    vo = analise['VOLUME'] >= analise['m_vol']
    boll = (analise['boll_hi'] - analise['CLOSE']) >= ((analise['boll_lo'] - analise['CLOSE'])*2)

    resultado = (int(rsi) + int(ad) + int(ma) + int(vo) + int(boll))
    if resultado >= 1:
        return True
    


def noti_telegram(token, chat_id, ativo):
    # Definir o token do seu bot
    bot = telebot.TeleBot(token)
    hoje = datetime.date.today()
    frase = f'{ativo} | {hoje} \n \U0001F4B8 \U0001F4B8 \U0001F4B8 \U0001F4B8 \U0001F4B8 \U0001F4B8 \U0001F4B8  \n O ativo tem boas perspectivas para compra na data de hoje de acordo com os indicadores técnicos do gráfico acima \u261D \u261D \u261D '
    # Abrir a imagem que você deseja enviar
    with open('grafico.png', 'rb') as photo:
        # Enviar a imagem para o chat
        bot.send_photo(chat_id, photo, caption=frase)
