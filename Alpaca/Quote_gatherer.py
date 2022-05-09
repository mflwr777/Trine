# Quote gatherer 

from os import access
from time import time
import config
from alpaca_trade_api.stream import Stream
from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd
import numpy as np

np.set_printoptions(edgeitems=25, linewidth=100000)
pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 600)
# working with pandas

api1 = REST(key_id=config.api_key,secret_key=config.api_secret_key,base_url=config.base_url)
api = REST(config.api_key,config.api_secret_key,config.base_url) 
quotes = api.get_quotes(config.symbols, "2021-06-08", "2021-06-10", limit=100000).df
quotes2 = api.get_latest_quote()

printer = pd.DataFrame.sort_index(axis=0)
print(printer)



exit()