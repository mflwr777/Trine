from email.quoprimime import quote
from lib2to3.pygram import Symbols
from smtplib import quotedata
from time import thread_time_ns
from InfrontConnect import infront
from scipy.fftpack import cc_diff
import config
from alpaca_trade_api.stream import Stream
import pandas as pd 
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width',100)


# Functions of channels - there are more! https://github.com/alpacahq/alpaca-trade-api-python
async def trade_callback(t):
    print('trade', t)
async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance - remove ping_interval for continous stream
stream = Stream(config.alpaca_api_total.id,
                config.alpaca_api_total.password,config.alpaca_api_total.base,config.alpaca_api_total.base)


# subscribing to event - mute one if wanting just trades or quotes 
stream.subscribe_quotes(quote_callback, config.tickerlist1)
# stream.subscribe_trades(trade_callback, config.tickerlist1)

runner = stream.run()