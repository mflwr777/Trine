import imp
from numpy import dtype, info
from pandas import DataFrame, period_range
import yfinance
import config
import yfinance as yf
from pandas import DataFrame as df
import file_reader_writer as frw
from functools import cache


active_tickers = yf.Tickers(frw.cef_prices) #multihandler
# active_ticker = yf.Ticker(frw.cef_navs) #single handler



history_gatherer = active_tickers.history(start = config.start_time, end=config.end_time)
# info_gatherer = active_ticker.info


output = DataFrame(history_gatherer)



