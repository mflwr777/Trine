from operator import le, mod
from numpy import append
import yfinance
from config import*
import pandas as pd
import itertools

sub_path = str(pathlib.Path(__file__).parent.resolve())
p = print

# Reading all cefs and converting them into a list 
cef_loader = pd.read_csv(sub_path + '\\ceflist.csv')['Symbol']
cef_price_tickers_uncurated = [cef_loader[n] for n in range(len(cef_loader.index))]
cef_navs_tickers_uncurated = ['X' + cef_price_tickers_uncurated[n] + 'X' for n in range(len(cef_loader.index))]
ticker_dict = {price_ticker: 'X' + price_ticker + 'X' for price_ticker in cef_loader.to_list()} # Dictionary comprehension



'Currating NAV tickers since rule above does not alway apply...not all inclusive to the csv file gathered form due to delisting etc'
missing_values = ('XPAXSX','XHGLBX','XFAXX','XENXX','XNBXGX','XMAVX','XNPFDX','XMEGIX','XGBABX','XFINSX','XFUNDX'
                  ,'XRMMZX','XSDHYX','XARDCX','XSPXXX','XDEXX','XBSTZX','XHIXX',
                  'XQQQXX','XASGIX','XFTX','XBXMXX','XXFLTX','XRFMZX','XETXX','XNMAIX','XBMEZX',
                  'XNKXX','XIHTAX','XIHITX','XTYX','XBCATX','XNMCOX',
                  'XADXX','XDYFNX','XNPCTX','XGRXX','XGFX','XNRGXX','XBCXX',
                  'XRMTX','XBIGZX','XHFROX','XDIAXX','XJHAAX','XKFX','XBGXX','XTEAFX','XPMXX',
                  'XRAX','XNDMOX','XFDEUX')

price_tickers = [ticker[1:-1] for ticker in missing_values] # String slicing + list comprehension
print(price_tickers)
                  
replacement_values = ('XPAAX','XHGLX','XFAPX','XENWX','XNBGX','XPMAX','XNPFX','XMEGI','XGBAX', 'XFINX','XFUNX',
                      'XRMMX','XSDHX','XADCX','XSSPX','XDEWX','XBSZX','XHGIX',
                      'XQQQX','XAGIX','XFUTX','XBXMX','XFLTX','XRFZX','XETTX','XNMAX','XBMZX',
                      'XNCMX','XHTAX','XHITX','XTYCX','XCATX','XNMCX',
                      'XADEX','XDFNX','XNPCX','XXGRX','XGFNX','XNRGX','XBCRX',
                      'XOTCX','XBIGX','XHFOX','XDIAX','XJAAX','XKFDX','XXBGX','XTEAX','XPMQX',
                      'XRAIX', 'XNDMX','XFDEX')

for i, ticker in enumerate(price_tickers):
    ticker_dict[ticker] = replacement_values[i]

keys_to_remove = ['MPV','CEF','NXDT','CHN','RCG','FTHY','PHYS','BANX','MIO','TBLD','TWN','BIGZ','CUBA','VCIF','MCI','TSI','EIC','OXLC','JOF','NMS','SSSS','NMAI','OCCI','MXF','ECC','GRF','PSLV',
                  'ECAT','INSI','DMA','PAXS','WDI','SPE','SPPP','NPFD','ASA','JEMD','GUG','MEGI','NBXG','CET','HYB','VMM','VCF']

for key in keys_to_remove:
    del ticker_dict[key]

# ticker_dict.pop('VMM','VCF')    #Popping out whatever is missing 
# for key, value in ticker_dict.items():
#     print(key + ': ' + value) 

polished_price_list = []
for key in ticker_dict.keys():
    polished_price_list.append(key)

polished_nav_list = []
for value in ticker_dict.values():
    polished_nav_list.append(value)

main_list_zipped = zip(polished_price_list,polished_nav_list)

main_list_list= list(main_list_zipped)
main_list = []
for sublist in main_list_list:
    for item in sublist:
        main_list.append(item)



#Final polished and nice list to feed to yahoo fin ... ! 
print(polished_price_list)
print(polished_nav_list)

print(len(polished_price_list))
print(len(polished_nav_list))
print((main_list))
     
' VEGARDS PRO TIPS BELOW'
# for i in range(len(missing_values)):
#     asd[missing_values[i]] = replacement_values[i]

# 'del asd['PAXS']   ##Deliting key-val pair from dict(insert key)
# dict.pop(key) #method 2 
# print('PAXS: ' + asd['PAXS'])    

# ''' vg's dict methods '''
# for key in asd.keys():
#     print(key)

# for value in asd.values():
#     print(value)

# for key, value in asd.items():
#     print(key + ': ' + value) 

# cef_navs_tickers_curated_list_list = (pd.DataFrame(cef_navs_tickers_uncurated).replace(to_replace=missing_values,value=replacement_values)).values.tolist() # this spits out list of list, want to make it to a simple list
# #Simplyfind to simple list 
# cef_navs_tickers_curated = list(itertools.chain(*cef_navs_tickers_curated_list_list))



'semi-curated dict'

# print(len(cef_navs_tickers_curated)) #458
# print(len(cef_price_tickers_uncurated)) #458


TESTLIST = [1,2,3,4,5]

print(ticker_dict)



