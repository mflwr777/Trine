from numpy import dtype
from pandas import DataFrame, period_range
import yfinance
import config
import yfinance as yf
from pandas import DataFrame as df
    

active_tickers = yf.Tickers(config.tickerlist1)
history_gatherer = active_tickers.history(start = config.start_time, end=config.end_time)
output = DataFrame(history_gatherer)


