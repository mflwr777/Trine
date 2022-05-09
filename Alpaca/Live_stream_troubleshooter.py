from alpaca_trade_api.stream import Stream
import config

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream(key_id=config.general_user_id,
                secret_key=config.general_password,
                base_url=config.general_base,
                data_feed=config.general_subscription)  # <- replace to SIP if you have PRO subscription



# subscribing to event
# stream.subscribe_trades(trade_callback, 'AAPL')
stream.subscribe_quotes(quote_callback,"TYG", "NTG", "SOR", "NDP", "FEI", "EMO", "NML", "IGR", "RQI", "CHY", "CHI", "CCD")


stream.run()