from config import*
from pandas import DataFrame as df
import file_reader as file_reader
from file_reader import*
import yfinance as yf


active_tickers = yf.Tickers(file_reader.cef_navs_tickers_curated) #multihandler
'active_ticker = yf.Ticker(frw.cef_navs) #single handler'



history_gatherer = active_tickers.history(period='max')
# info_gatherer = active_ticker.info


output = pd.DataFrame(history_gatherer)