


import pickle
import os
import requests
import json
import time
import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import pickle
import requests
import yaml
import yfinance as yf
import pandas as pd
import dateutil.relativedelta
import numpy as np

from datetime import date
from datetime import datetime
import datetime as dt

from tvScrape import TvScrape, Interval
tv = TvScrape()

holdingsdir = os.path.join(os.getcwd(),'Holdings')
tickers = pd.read_csv(os.path.join(holdingsdir, 'holdings_all.csv'), header=0, sep=',')


# index
spx = tv.get_hist(symbol="SPX",exchange="SP",interval='1D',n_bars=250, extended_session=False)

def load_from_tvscrape(ticker,  exchange_='NYSE', number_bars=250, benchmark=spx):
    # Get historical data
    data = tv.get_hist(symbol=ticker, exchange=exchange_, interval='1D', n_bars=number_bars)
    data['Ticker']=ticker
    data['date'] = data.index.date
    data['relative']=data.close/benchmark.close
    data['3EMA']=data['close'].ewm(span=3,adjust=False).mean()
    # also calculate the simple moving average
    data['3SMA']=data['close'].rolling(window=3).mean()
    data['5EMA']=data['close'].ewm(span=5,adjust=False).mean()
    data['12EMA']=data['close'].ewm(span=12,adjust=False).mean()
    data['21EMA']=data['close'].ewm(span=20,adjust=False).mean()
    data['50EMA']=data['close'].ewm(span=50,adjust=False).mean()
    data['63EMA']=data['close'].ewm(span=63,adjust=False).mean()
    data['144EMA']=data['close'].ewm(span=144,adjust=False).mean()
    data['r3EMA']=data['relative'].ewm(span=3,adjust=False).mean()
    data['r3SMA']=data['relative'].rolling(window=3).mean()
    data['r12EMA']=data['relative'].ewm(span=12,adjust=False).mean()
    data['r21EMA']=data['relative'].ewm(span=20,adjust=False).mean()
    data['r50EMA']=data['relative'].ewm(span=50,adjust=False).mean()
    data['r63EMA']=data['relative'].ewm(span=63,adjust=False).mean()
    data['r144EMA']=data['relative'].ewm(span=144,adjust=False).mean()
    return data

def ema(hist,period=5):
    return hist['Close'].ewm(span=period,adjust=False).mean()

def gain_3ema(hist,period=5):
    return hist['3EMA'].pct_change(period)*100


def gain_close(hist,period=5):
    return hist['Close'].pct_change(period)*100


tickers_df = pd.DataFrame(columns=['Ticker','ETF', 'ETFInSPX','5EMA','12EMA','50EMA','144EMA'])

ticker = tickers.iloc[0]['Symbol']
ticker='XOM'
symbol = yf.Ticker(ticker)




hist = symbol.history(period="12mo")
histhour = symbol.history(period="10d", interval='60m')


hist['3EMA']=ema(hist,3) 
hist['5EMA']=ema(hist,5)
hist['12EMA']=ema(hist,12)
hist['50EMA']=ema(hist,50)
hist['144EMA']=ema(hist,144)
hist['5dgain']=gain_3ema(hist)
hist['5dgainclose']=gain_close(hist)

symbol.info['forwardPE']
symbol.info['marketCap']
symbol.info['fiftyTwoWeekLow']
symbol.info['fiftyTwoWeekHigh']
symbol.info['fiftyDayAverage']
symbol.info['twoHundredDayAverage']

# plot
hist[['Close','12EMA','50EMA','144EMA']].plot(figsize=(10,5))

symbollist = [num for num in tickers.iloc[0]] + [hist['5EMA'].iloc[-1],hist['12EMA'].iloc[-1],hist['12EMA'].iloc[-1],hist['50EMA'].iloc[-1]hist['144EMA'].iloc[-1]]
# append testlist to tickers_df
tickers_df.loc[len(tickers_df)] = symbollist


