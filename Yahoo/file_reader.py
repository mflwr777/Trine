from operator import le
import yfinance
from config import*
import pandas as pd
sub_path = str(pathlib.Path(__file__).parent.resolve())
p = print

# Reading all cefs and converting them into a list 
cef_loader = pd.read_csv(sub_path + '\\ceflist.csv')['Symbol']
cef_price_tickers_uncurated = [cef_loader[n] for n in range(len(cef_loader.index))]
cef_navs_tikcers_uncurated = ['X' + cef_price_tickers_uncurated[n] + 'X' for n in range(len(cef_loader.index))]




'Currating NAV tickers since rule above does not alway apply...not all inclusive to the csv file gathered form due to delisting etc'
missing_values = ('XPAXSX','XHGLBX','XFAXX','XENXX','XNBXGX','XMAVX','XNPFDX','XMEGIX','XGBABX','XFINSX','XFUNDX'
                  ,'XRMMZX','XSDHYX','XARDCX','XSPXXX','XDEXX','XBSTZX','XHIXX',
                  'XQQQXX','XASGIX','XFTX','XBXMXX','XXFLTX','XRFMZX','XETXX','XNMAIX','XBMEZX',
                  'XNKXX','XIHTAX','XIHITX','XTYX','XBCATX','XNMCOX',
                  'XADXX','XDYFNX','XNPCTX','XGRXX','XGFX','XNRGXX','XBCXX',
                  'XRMTX','XBIGZX','XHFROX','XDIAXX','XJHAAX','XKFX','XBGXX','XTEAFX','XPMXX',
                  'XRAX','XNDMOX','XFDEUX')
                  
replacement_values = ('XPAAX','XHGLX','XFAPX','XENWX','XNBGX','XPMAX','XNPFX','XMEGI','XGBAX', 'XFINX','XFUNX',
                      'XRMMX','XSDHX','XADCX','XSSPX','XDEWX','XBSZX','XHGIX',
                      'XQQQX','XAGIX','XFUTX','XBXMX','XFLTX','XRFZX','XETTX','XNMAX','XBMZX',
                      'XNCMX','XHTAX','XHITX','XTYCX','XCATX','XNMCX',
                      'XADEX','XDFNX','XNPCX','XXGRX','XGFNX','XNRGX','XBCRX',
                      'XOTCX','XBIGX','XHFOX','XDIAX','XJAAX','XKFDX','XXBGX','XTEAX','XPMQX',
                      'XRAIX', 'XNDMX','XFDEX')

cef_navs_tickers_curated = (pd.DataFrame(cef_navs_tikcers_uncurated).replace(to_replace=missing_values,value=replacement_values)).values.tolist()

'semi-curated dict'

print(len(cef_navs_tickers_curated))
print(len(cef_price_tickers_uncurated))


# price_to_nav_dict = {cef_price_tickers_uncurated[n]: cef_navs_tickers_curated[n] for n in range(len(cef_navs_tickers_curated))}




# print(cef_navs_tickers_curated)


# print ("Dict key-value are : ")
# print([(k, price_nav_dict[k]) for k in price_nav_dict])


'''trashbin'''

# nav_to_price_dict ={cef_navs_tikcers_uncurated[n]: cef_price_tickers_uncurated[n] for n in range(len(cef_price_tickers_uncurated))}