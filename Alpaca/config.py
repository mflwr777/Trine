### Change alpaca..id, alpaca..password,
from pickle import NONE
from symtable import Symbol
from alpaca_trade_api.rest import REST, TimeFrame
from matplotlib.axis import Ticker 

# Just some tickerlist - they might be refered somewhere else so be chill with editing 
tickerlist1 = "TYG", "NTG", "SOR", "NDP", "FEI", "EMO", "NML", "IGR", "RQI", "CHY", "CHI", "CCD" #In production
tickerlist2 = "TYG", "NTG", "SOR"
tickerlist3 = "TYG", "NTG", "SOR", "NDP", "FEI", "EMO", "NML", "IGR", "RQI", "CHY", "CHI", "CCD"
tickerlist4 = "TYG", "NTG", "SOR", "NDP", "FEI", "EMO", "NML", "IGR", "RQI", "CHY", "CHI", "CCD"
tickerlist5 = ''
tickerlist6 = ''

# Change me if necessary 
general_user_id = 'AKDOQNRFH36Q5UHI7J19'
general_password = 'JBXmadGA8lE29aVBuHVO2rx8LJWN9gzzAXiC8Kdh'
general_base = 'https://data.alpaca.markets/v2'
general_subscription = 'sip' #for tracking iex markets -- 
ENDPOINT = 'https://api.alpaca.markets' # Not sure where it is used tbh ... !


start_time = None
end_time = None
ping_interval = {'ping_interval': 1} # Not used 


#Alpacca api_configs - edit possible! 
class Feeds:
    def __init__(self,id,password,base,subscription):
        self.id = id
        self.password = password
        self.base = base
        self.subscription = subscription

class Tickers:
    def __init__(self,name,content):
        self.name = name
        self.content = content

#Note to self: 
    # def __str__(self):
    #     return self.name
    
    # def __eq__(self, __o: object) -> bool:
    #     return (self.name == o.name) and (self.content == o.content)




# Fixing Feed classes 
alpaca_api_iex = Feeds(general_user_id,general_password,general_base,general_subscription,)
alpaca_api_total = Feeds(general_user_id,general_password,general_base,'sip')
polygon_api = Feeds(None,None,None,None)
infront_api = Feeds(None,None,None,None)

# Fixing Tickers classes
tickers_production = Tickers('production',tickerlist1)
tickers_alternative = Tickers('alternative',tickerlist2)
tickers_stalker = Tickers('stalker', tickerlist3)



# Do not edit ... !! 
dict_exchange = {'A':'NYSE American (AMEX)',
                'B':'NASDAQ OMX BX',
                'C':'National Stock Exchange',
                'D':'FINRA ADF', 
                'E':'Market Independent',
                'H':'MIAX',
                'I':'International Security Exhange',
                'J':'Cboe EDGA', 
                'K':'CBOE', 
                'L':'Long Term Stock Exhangem', 
                'M':'Chicago Stock Exhnage', 
                'N':'New York Stock Exchange',
                'P':'NYSE Arca','Q':'NASDAQ OMX', 
                'S':'NASDAQ Small Cap', 
                'T':'Nasdaq Int',
                'U':'Members Exchange',
                'V':'IEX',
                'W':'CBOE',
                'X':'NASDAQ OMX PSX',
                'Y':'CBOE BYX',
                'Z':'CBOE BZX'}
dict_tickers = {'production':tickerlist1, 'alternative':tickerlist2,'stalker':tickerlist3}


