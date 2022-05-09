import csv
from dataclasses import replace
from email.quoprimime import quote
from importlib.resources import path
from operator import index
from sqlite3 import Timestamp
from xmlrpc.client import SafeTransport
from matplotlib import container, ticker
from matplotlib.pyplot import get
from alpaca_trade_api import Stream
import numpy as np  
import pandas as pd
import config
from alpaca_trade_api.rest import REST, TimeFrame
from datetime import datetime
from importlib.resources import path
import pathlib
import config
from functools import cache

sub_path = str(pathlib.Path(__file__).parent.resolve())

'YYYY-MM-DD'
start_time = '2022-05-05' 
end_time = '2022-05-05' 


authenticator_iex = REST(config.alpaca_api_iex.id,config.alpaca_api_iex.password,config.alpaca_api_iex.base)
authenticator_total = REST(config.alpaca_api_total.id,config.alpaca_api_total.password,config.alpaca_api_total.base)


# Intilize tickerlist that you want to use: ticerlist_production, tickers_alternative, tickers_stalker => Check config to see what's what (or dict) 
active_tickers = config.tickers_production


#''' bars = authenticator.get_bars(tickerlist_production,start=start_time, end=end_time, limit= 200000).df #Broken? Need on e more entry idk'''
trades_iex = authenticator_iex.get_trades(active_tickers.content, start= start_time, end= end_time, limit= 10).df 
quotes_iex = authenticator_iex.get_quotes(active_tickers.content, start= start_time, end= end_time, limit= 10).df 
trades_total = authenticator_total.get_trades(active_tickers.content, start = start_time, end = end_time, limit = 10).df
quotes_total = authenticator_total.get_quotes(active_tickers.content, start = start_time, end = end_time, limit = 10).df

# Initlize what to track - _iex trades, quotes or _total_ quotes or trades


dtf = pd.DataFrame(quotes_total)

def sub_path_namer(input):
    if input.equals(pd.DataFrame(trades_iex)):
        return 'iex'
    elif input.equals(pd.DataFrame(quotes_iex)):
        return 'iex'
    elif input.equals(pd.DataFrame(trades_total)):
        return 'total'
    elif input.equals(pd.DataFrame(quotes_total)):
        return 'total'
    else:
        return 'I dont understand'


# reader_container = sub_path + '\Historical_trades\\' + 'str(sub_path_namer(inner_ref))' + '\\' +str(active_tickers.name)+ str(start_time) + '.csv'


# experiemtal_writer = dtf.to_csv(reader_container,index=True) #The csv writer 

# print(reader_container) 


print(sub_path_namer(12312313))