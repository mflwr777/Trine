#Hsitory gatherer
'https://github.com/alpacahq/alpaca-trade-api-python'
from asyncore import read
import config
from config import*

### Non editable settings 
np.set_printoptions(edgeitems=25, linewidth=100000)
pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 600)
# lil' pathfinder
sub_path = str(pathlib.Path(__file__).parent.resolve())
sub_path_dropbox = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve())

#Creating authenticator 
authenticator_iex = REST(config.alpaca_api_iex.id,config.alpaca_api_iex.password,config.alpaca_api_iex.base)
authenticator_total = REST(config.alpaca_api_total.id,config.alpaca_api_total.password,config.alpaca_api_total.base)
# Spits out where you are (should be - used for writer .. )

'YYYY-MM-DD'
start_time = '2022-05-12' 
end_time = '2022-05-12' 


# Intilize tickerlist that you want to use: ticerlist_production, tickers_alternative, tickers_stalker => Check config to see what's what (or dict) 
active_tickers = config.tickers_production


#''' bars = authenticator.get_bars(tickerlist_production,start=start_time, end=end_time, limit= 200000).df #Broken? Need on e more entry idk'''
trades_iex = authenticator_iex.get_trades(active_tickers.content, start= start_time, end= end_time, limit= 300000).df 
quotes_iex = authenticator_iex.get_quotes(active_tickers.content, start= start_time, end= end_time, limit= 300000).df 
trades_total = authenticator_total.get_trades(active_tickers.content, start = start_time, end = end_time, limit = 300000).df
quotes_total = authenticator_total.get_quotes(active_tickers.content, start = start_time, end = end_time, limit = 300000).df

# Initlize what to track - _iex trades, quotes or _total_ quotes or trades
dtf = trades_total

# def sub_path_namer(inner_ref):
#     if inner_ref.equals(trades_iex):
#         return 'iex'
#     elif inner_ref.equals(quotes_iex):
#         return 'iex'
#     elif inner_ref.equals(trades_total):
#         return 'total'
#     elif inner_ref.equals(quotes_total):
#         return 'total'


reader_container_csv_iex = sub_path + '\Historical_trades\\' + '\\' +str(active_tickers.name)+ str(start_time) +'iex_TEST'+'.csv'
reader_container_csv_total = sub_path + '\Historical_trades\\' + '\\' +str(active_tickers.name)+ str(start_time) +'.csv'

reader_container_dropbox = 'C:\\Users\\march\\Dropbox\\SpekulanterUdenGrænser\\Nicolas\\Trinelise\\IEX\\production_v1_0522\\csv' + '\\' +str(active_tickers.name)+ str(start_time) +'.csv'
# # # reader_container_JSON = sub_path + '\Historical_trades\\' + '\\' +str(active_tickers.name)+ str(start_time) + '.JSON'

experiemtal_writer_csv = dtf.to_csv(reader_container_dropbox,index=True) #The csv writer 
# # # expermiental_writer_JSON = dtf.to_json(reader_container_JSON,index=False) #JSON writer

# print(sub_path)
print(sub_path_dropbox)
print(reader_container_dropbox)