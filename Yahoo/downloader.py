from config import*
from pandas import DataFrame as df
import file_reader as file_reader
from file_reader import*
import yfinance as yf
sub_path = str(pathlib.Path(__file__).parent.resolve())
sub_path_dropbox = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve())


''' Initilize active tickers list '''
active_tickers = yf.Tickers(file_reader.main_list)
'active_ticker = yf.Ticker(frw.cef_navs) #single handler'

history_gatherer = active_tickers.history(period='max')
# distribution_gatherer = active_tickers.history(''period='2021-09-24', actions='dividends''')

# info_gatherer = active_ticker.info
output = pd.DataFrame(history_gatherer) #choose output, what to gather? 


reader_container_dropbox = 'C:\\Users\\march\\Dropbox\\SpekulanterUdenGrænser\\Nicolas\\Trinelise\\IEX\\production_v1_0522\\csv\\' + 'cef_price_nav20220520' +'.csv'
writer = output.to_csv(reader_container_dropbox,index=True) #The csv writer 

