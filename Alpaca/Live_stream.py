from email.quoprimime import quote
from lib2to3.pygram import Symbols
from smtplib import quotedata
from time import thread_time_ns
import config
from alpaca_trade_api.stream import Stream
import sys
import pandas as pd 
import websocket
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width',100)


# Functions of channels - there are more! https://github.com/alpacahq/alpaca-trade-api-python
async def trade_callback(t):
    print('trade', t)
async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream_iex = Stream(config.alpaca_api_iex.id,
                config.alpaca_api_iex.password,
                config.alpaca_api_iex.base,
                config.alpaca_api_iex.subscription)
stream_total = Stream(config.alpaca_api_total.id,
                config.alpaca_api_total.password,
                config.alpaca_api_total.base,
                config.alpaca_api_total.subscription)


# # # subscribing to event - mute one if wanting just trades or quotes # # # 
stream_iex.subscribe_quotes(quote_callback, config.tickerlist1)
stream_total.subscribe_quotes(quote_callback, config.tickerlist1)
stream_iex.subscribe_trades(trade_callback,config.tickerlist1)
stream_total.subscribe_quotes(trade_callback,config.tickerlist1)

'stream.subscribe_trades(trade_callback, config.tickerlist1)'
runner = stream_iex.run()
print(runner)


