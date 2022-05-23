from alpaca_trade_api.stream import Stream
import config
import sys 

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream(key_id=config.general_user_id,
                secret_key=config.general_password,
                base_url=config.general_base,
                data_feed=config.premium_subscription)  # <- replace to SIP if you have PRO subscription



# subscribing to event
# stream.subscribe_trades(trade_callback, 'AAPL')

''' Uncomment for production incase config.tickers_productions is closed down'''

stream.subscribe_quotes(quote_callback,"TYG", "NTG", "SOR", "NDP", "FEI", "EMO", "NML", "IGR", "RQI", "CHY", "CHI", "CCD")

# stream.subscribe_quotes(quote_callback,(config.tickers_production))
runner = stream.run()

## Kladdeark ### 
import sys
with open('C:\\Users\\march\\Desktop\\toaster.txt', 'w') as f:
    sys.stdout = f
    print(str(stream.run))