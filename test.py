


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

# read tickers.csv
def read_tickers():
   tickers = pd.read_csv('tickers.csv')
   return tickers

tickers=read_tickers()

# index
spx = tv.get_hist(symbol="SPX",exchange="SP",interval='1D',n_bars=250, extended_session=False)



def load_data(ticker,  exchange_='NYSE', number_bars=250, benchmark=spx):
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

ticker_='ABNB'
exchange_='NASDAQ'

list_columns = ['Ticker', 'Exchange','Close']
list_append = list()

test=pd.read_csv('tickers.csv')

list_append = list()
filter = test.Exchange.isna()

multiplier=12
batchsize=100
for asset_index in test[filter].index[multiplier*batchsize:(multiplier+1)*batchsize]:
    # try with NASDAQ, else try with NYSE. put the one that works in a list
    ticker = test[filter].loc[asset_index,:]['ticker']
    etf = test[filter].loc[asset_index,:]['ETF']
    print(ticker,etf)
    try:
        df = load_data(ticker, 'NASDAQ', number_bars=10)
        list_append.append([ticker,etf, 'NASDAQ'])
    except:
        try:
            df = load_data(ticker, 'NYSE', number_bars=10)
            list_append.append([ticker,etf, 'NYSE'])
        except:
            print(f'Error with {ticker}')
            list_append.append([ticker, etf,0])

# write list_append to a csv
print('Done!')
df = pd.DataFrame(list_append, columns=['Ticker', 'ETF', 'Exchange'])
df.to_csv('test.csv',index=False)


load_data('CFR', exchange_= 'NYSE', number_bars=10)