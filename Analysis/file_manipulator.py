import datetime
from importlib.resources import path
from types import TracebackType
import pandas as pd
import itertools
import pathlib
import pickle
import numpy as np


sub_path = str(pathlib.Path(__file__).parent.resolve())
parent_path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve()) #Gives c:\\Users\\___CurrentUser____

# #Dict for final setup .. @ C:\Users\march\Dropbox\SpekulanterUdenGrænser\Nicolas\Trinelise\Yahoo scraper
ticker_dict = {'ACP': 'XACPX', 'ACV': 'XACVX', 'ADX': 'XADEX', 'AEF': 'XAEFX', 'AFB': 'XAFBX', 'AFT': 'XAFTX', 'AGD': 'XAGDX', 'AIF': 'XAIFX', 'AIO': 'XAIOX', 'AOD': 'XAODX', 'ARDC': 'XADCX', 'ASG': 'XASGX', 'ASGI': 'XAGIX', 'AVK': 'XAVKX', 'AWF': 'XAWFX', 'AWP': 'XAWPX', 'BBN': 'XBBNX', 'BCAT': 'XCATX', 'BCV': 'XBCVX', 'BCX': 'XBCRX', 'BDJ': 'XBDJX', 'BFK': 'XBFKX', 'BFZ': 'XBFZX', 'BGB': 'XBGBX', 'BGH': 'XBGHX', 'BGR': 'XBGRX', 'BGT': 'XBGTX', 'BGX': 'XXBGX', 'BGY': 'XBGYX', 'BHK': 'XBHKX', 'BHV': 'XBHVX', 'BIF': 'XBIFX', 'BIT': 'XBITX', 'BKN': 'XBKNX', 'BKT': 'XBKTX', 'BLE': 'XBLEX', 'BLW': 'XBLWX', 'BME': 'XBMEX', 'BMEZ': 'XBMZX', 'BNY': 'XBNYX', 'BOE': 'XBOEX', 'BRW': 'XBRWX', 'BSL': 'XBSLX', 'BST': 'XBSTX', 'BSTZ': 'XBSZX', 'BTA': 'XBTAX', 'BTO': 'XBTOX', 'BTT': 'XBTTX', 'BTZ': 'XBTZX', 'BUI': 'XBUIX', 'BWG': 'XBWGX', 'BXMX': 'XBXMX', 'BYM': 'XBYMX', 'CAF': 'XCAFX', 'CBH': 'XCBHX', 'CCD': 'XCCDX', 'CEE': 'XCEEX', 'CEM': 'XCEMX', 'CEN': 'XCENX', 'CEV': 'XCEVX', 'CGO': 'XCGOX', 'CHI': 'XCHIX', 'CHW': 'XCHWX', 'CHY': 'XCHYX', 'CIF': 'XCIFX', 'CII': 'XCIIX', 'CIK': 'XCIKX', 'CLM': 'XCLMX', 'CMU': 'XCMUX', 'CPZ': 'XCPZX', 'CRF': 'XCRFX', 'CSQ': 'XCSQX', 'CTR': 'XCTRX', 'CXE': 'XCXEX', 'CXH': 'XCXHX', 'DBL': 'XDBLX', 'DCF': 'XDCFX', 'DDF': 'XDDFX', 'DEX': 'XDEWX', 'DFP': 'XDFPX', 'DHF': 'XDHFX', 'DHY': 'XDHYX', 'DIAX': 'XDIAX', 'DLY': 'XDLYX', 'DMB': 'XDMBX', 'DMF': 'XDMFX', 'DMO': 'XDMOX', 'DNP': 'XDNPX', 'DPG': 'XDPGX', 'DSL': 'XDSLX', 'DSM': 'XDSMX', 'DSU': 'XDSUX', 'DTF': 'XDTFX', 'DYFN': 'XDFNX', 'EAD': 'XEADX', 'ECF': 'XECFX', 'EDD': 'XEDDX', 'EDF': 'XEDFX', 'EDI': 'XEDIX', 'EEA': 'XEEAX', 'EFL': 'XEFLX', 'EFR': 'XEFRX', 'EFT': 'XEFTX', 'EGF': 'XEGFX', 'EHI': 'XEHIX', 'EIM': 'XEIMX', 'EMD': 'XEMDX', 'EMF': 'XEMFX', 'EMO': 'XEMOX', 'ENX': 'XENWX', 'EOD': 'XEODX', 'EOI': 'XEOIX', 'EOS': 'XEOSX', 'EOT': 'XEOTX', 'ERC': 'XERCX', 'ERH': 'XERHX', 'ETB': 'XETBX', 'ETG': 'XETGX', 'ETJ': 'XETJX', 'ETO': 'XETOX', 'ETV': 'XETVX', 'ETW': 'XETWX', 'ETX': 'XETTX', 'ETY': 'XETYX', 'EVF': 'XEVFX', 'EVG': 'XEVGX', 'EVM': 'XEVMX', 'EVN': 'XEVNX', 'EVT': 'XEVTX', 'EVV': 'XEVVX', 'EXD': 'XEXDX', 'EXG': 'XEXGX', 'FAM': 'XFAMX', 'FAX': 'XFAPX', 'FCO': 'XFCOX', 'FCT': 'XFCTX', 'FDEU': 'XFDEX', 'FEI': 'XFEIX', 'FEN': 'XFENX', 'FEO': 'XFEOX', 'FFA': 'XFFAX', 'FFC': 'XFFCX', 'FGB': 'XFGBX', 'FIF': 'XFIFX', 'FINS': 'XFINX', 'FLC': 'XFLCX', 'FMN': 'XFMNX', 'FMO': 'XFMOX', 'FMY': 'XFMYX', 'FOF': 'XFOFX', 'FPF': 'XFPFX', 'FPL': 'XFPLX', 'FRA': 'XFRAX', 'FSD': 'XFSDX', 'FT': 'XFUTX', 'FTF': 'XFTFX', 'FUND': 'XFUNX', 'GAB': 'XGABX', 'GAM': 'XGAMX', 'GBAB': 'XGBAX', 'GCV': 'XGCVX', 'GDL': 'XGDLX', 'GDO': 'XGDOX', 'GDV': 'XGDVX', 'GER': 'XGERX', 'GF': 'XGFNX', 'GGN': 'XGGNX', 'GGT': 'XGGTX', 'GGZ': 'XGGZX', 'GHY': 'XGHYX', 'GIM': 'XGIMX', 'GLO': 'XGLOX', 'GLQ': 'XGLQX', 'GLU': 'XGLUX', 'GLV': 'XGLVX', 'GNT': 'XGNTX', 'GOF': 'XGOFX', 'GRX': 'XXGRX', 'GUT': 'XGUTX', 'HEQ': 'XHEQX', 'HFRO': 'XHFOX', 'HGLB': 'XHGLX', 'HIE': 'XHIEX', 'HIO': 'XHIOX', 'HIX': 'XHGIX', 'HNW': 'XHNWX', 'HPF': 'XHPFX', 'HPI': 'XHPIX', 'HPS': 'XHPSX', 'HQH': 'XHQHX', 'HQL': 'XHQLX', 'HTD': 'XHTDX', 'HTY': 'XHTYX', 'HYI': 'XHYIX', 'HYT': 'XHYTX', 'IAE': 'XIAEX', 'IAF': 'XIAFX', 'IDE': 'XIDEX', 'IFN': 'XIFNX', 'IGA': 'XIGAX', 'IGD': 'XIGDX', 'IGI': 'XIGIX', 'IGR': 'XIGRX', 'IHD': 'XIHDX', 'IHIT': 'XHITX', 'IHTA': 'XHTAX', 'IIF': 'XIIFX', 'IIM': 'XIIMX', 'IQI': 'XIQIX', 'IRL': 'XIRLX', 'ISD': 'XISDX', 'IVH': 'XIVHX', 'JCE': 'XJCEX', 'JCO': 'XJCOX', 'JEQ': 'XJEQX', 'JFR': 'XJFRX', 'JGH': 'XJGHX', 'JHAA': 'XJAAX', 'JHI': 'XJHIX', 'JHS': 'XJHSX', 'JLS': 'XJLSX', 'JMM': 'XJMMX', 'JPC': 'XJPCX', 'JPI': 'XJPIX', 'JPS': 'XJPSX', 'JPT': 'XJPTX', 'JQC': 'XJQCX', 'JRI': 'XJRIX', 'JRO': 'XJROX', 'JRS': 'XJRSX', 'JSD': 'XJSDX', 'KF': 'XKFDX', 'KIO': 'XKIOX', 'KMF': 'XKMFX', 'KSM': 'XKSMX', 'KTF': 'XKTFX', 'KYN': 'XKYNX', 'LDP': 'XLDPX', 'LEO': 'XLEOX', 'LGI': 'XLGIX', 'MAV': 'XPMAX', 'MCA': 'XMCAX', 'MCN': 'XMCNX', 'MCR': 'XMCRX', 'MFD': 'XMFDX', 'MFL': 'XMFLX', 'MFM': 'XMFMX', 'MFV': 'XMFVX', 'MGF': 'XMGFX', 'MGU': 'XMGUX', 'MHD': 'XMHDX', 'MHF': 'XMHFX', 'MHI': 'XMHIX', 'MHN': 'XMHNX', 'MIN': 'XMINX', 'MIY': 'XMIYX', 'MMD': 'XMMDX', 'MMT': 'XMMTX', 'MMU': 'XMMUX', 'MNP': 'XMNPX', 'MPA': 'XMPAX', 'MQT': 'XMQTX', 'MQY': 'XMQYX', 'MSD': 'XMSDX', 'MUA': 'XMUAX', 'MUC': 'XMUCX', 'MUE': 'XMUEX', 'MUI': 'XMUIX', 'MUJ': 'XMUJX', 'MVF': 'XMVFX', 'MVT': 'XMVTX', 'MXE': 'XMXEX', 'MYC': 'XMYCX', 'MYD': 'XMYDX', 'MYI': 'XMYIX', 'MYJ': 'XMYJX', 'MYN': 'XMYNX', 'NAC': 'XNACX', 'NAD': 'XNADX', 'NAN': 'XNANX', 'NAZ': 'XNAZX', 'NBB': 'XNBBX', 'NBH': 'XNBHX', 'NBO': 'XNBOX', 'NBW': 'XNBWX', 'NCA': 'XNCAX', 'NCV': 'XNCVX', 'NCZ': 'XNCZX', 'NDMO': 'XNDMX', 'NDP': 'XNDPX', 'NEA': 'XNEAX', 'NEV': 'XNEVX', 'NFJ': 'XNFJX', 'NHS': 'XNHSX', 'NID': 'XNIDX', 'NIE': 'XNIEX', 'NIM': 'XNIMX', 'NIQ': 'XNIQX', 'NKG': 'XNKGX', 'NKX': 'XNCMX', 'NMCO': 'XNMCX', 'NMI': 'XNMIX', 'NML': 'XNMLX', 'NMT': 'XNMTX', 'NMZ': 'XNMZX', 'NNY': 'XNNYX', 'NOM': 'XNOMX', 'NPCT': 'XNPCX', 'NPV': 'XNPVX', 'NQP': 'XNQPX', 'NRGX': 'XNRGX', 'NRK': 'XNRKX', 'NRO': 'XNROX', 'NSL': 'XNSLX', 'NTG': 'XNTGX', 'NUO': 'XNUOX', 'NUV': 'XNUVX', 'NUW': 'XNUWX', 'NVG': 'XNVGX', 'NXC': 'XNXCX', 'NXJ': 'XNXJX', 'NXN': 'XNXNX', 'NXP': 'XNXPX', 'NZF': 'XNZFX', 'OIA': 'XOIAX', 'OPP': 'XOPPX', 'PAI': 'XPAIX', 'PCF': 'XPCFX', 'PCK': 'XPCKX', 'PCM': 'XPCMX', 'PCN': 'XPCNX', 'PCQ': 'XPCQX', 'PDI': 'XPDIX', 'PDO': 'XPDOX', 'PDT': 'XPDTX', 'PEO': 'XPEOX', 'PFD': 'XPFDX', 'PFL': 'XPFLX', 'PFN': 'XPFNX', 'PFO': 'XPFOX', 'PGP': 'XPGPX', 'PGZ': 'XPGZX', 'PHD': 'XPHDX', 'PHK': 'XPHKX', 'PHT': 'XPHTX', 'PIM': 'XPIMX', 'PMF': 'XPMFX', 'PML': 'XPMLX', 'PMM': 'XPMMX', 'PMO': 'XPMOX', 'PMX': 'XPMQX', 'PNF': 'XPNFX', 'PNI': 'XPNIX', 'PPT': 'XPPTX', 'PSF': 'XPSFX', 'PTA': 'XPTAX', 'PTY': 'XPTYX', 'PYN': 'XPYNX', 'PZC': 'XPZCX', 'QQQX': 'XQQQX', 'RA': 'XRAIX', 'RCS': 'XRCSX', 'RFI': 'XRFIX', 'RFM': 'XRFMX', 'RFMZ': 'XRFZX', 'RGT': 'XRGTX', 'RIV': 'XRIVX', 'RMI': 'XRMIX', 'RMM': 'XRMMX', 'RMMZ': 'XRMMX', 'RMT': 'XOTCX', 'RNP': 'XRNPX', 'RQI': 'XRQIX', 'RSF': 'XRSFX', 'RVT': 'XRVTX', 'SBI': 'XSBIX', 'SCD': 'XSCDX', 'SDHY': 'XSDHX', 'SMM': 'XSMMX', 'SOR': 'XSORX', 'SPXX': 'XSSPX', 'SRV': 'XSRVX', 'STK': 'XSTKX', 'SWZ': 'XSWZX', 'SZC': 'XSZCX', 'TDF': 'XTDFX', 'TEAF': 'XTEAX', 'TEI': 'XTEIX', 'THQ': 'XTHQX', 'THW': 'XTHWX', 'TPZ': 'XTPZX', 'TTP': 'XTTPX', 'TY': 'XTYCX', 'TYG': 'XTYGX', 'USA': 'XUSAX', 'UTF': 'XUTFX', 'UTG': 'XUTGX', 'VBF': 'XVBFX', 'VCV': 'XVCVX', 'VFL': 'XVFLX', 'VGI': 'XVGIX', 'VGM': 'XVGMX', 'VKI': 'XVKIX', 'VKQ': 'XVKQX', 'VLT': 'XVLTX', 'VMO': 'XVMOX', 'VPV': 'XVPVX', 'VTN': 'XVTNX', 'VVR': 'XVVRX', 'WEA': 'XWEAX', 'WIA': 'XWIAX', 'WIW': 'XWIWX', 'XFLT': 'XFLTX', 'ZTR': 'XZTRX'}
ticker_dict_m1_key = [*ticker_dict] #Prices non-formated
ticker_dict_m1_key = ['Close' + ticker_dict_m1_key[n] for n in range(len(ticker_dict_m1_key))]
ticker_dict_m1_values = list(ticker_dict.values())
ticker_dict_m1_values = ['Close' + ticker_dict_m1_values[n] for n in range(len(ticker_dict_m1_values))]
'm1 keys and m1 values include #Close+ticker/NAV name'

#Creating a new dictornary for this sub-proejct (creating disc values as pct of nav)
ticker_dict_mod = {ticker_dict_m1_key[n]:ticker_dict_m1_values[n] for n in range(len(ticker_dict_m1_key))}

csv_reader = pd.read_csv(r'C:\\Users\\march\\Dropbox\\SelandiaCapital\\Nicolas\\Trinelise\\Analysis_supplement\\cef_price_nav20220520_mod1.csv',low_memory=False)
df = pd.DataFrame(csv_reader)

print(df['CloseAFT'].isna().sum())
print(df['CloseADX'].isna().sum())

### Not wasting time on this - manually removing the dates from the CSV file ...###




'Saved a pkl object, no need to reruncode below ...!  pkl file sucks anyways so fuck it '
# csv_reads = pd.DataFrame(pd.read_csv(sub_path + '\\cef_price_nav20220520_mod1.csv',low_memory=False))
# csv_reads.to_pickle('cef_price_nav_mod1.pkl') 

# #Fuck this shit nigger....! Save as csv and fuck offfffffff..........................Also clean this mafaakkafile 
# df = pd.DataFrame(pd.read_csv(parent_path + '\\Dropbox\\SpekulanterUdenGrænser\\Nicolas\\Trinelise\\Analysis_supplement\\cef_price_nav_mod1.pkl'))
# pd.DataFrame(pd.read_pickle(parent_path + '\\Dropbox\\SpekulanterUdenGrænser\\Nicolas\\Trinelise\\Analysis_supplement\\cef_price_nav_mod1.pkl' )) #current dataframe ..! Noncut
# df_sub = (df.iloc[10124:, 1:]).astype(np.float32) #Shorten it to start 5/mai/2022
# print(df_sub['CloseASGI'])

''' Solution is to NOT pickle that shit up - but whatever carrying on => '''
# df = df.astype(np.float32)
# print((df))
# df = df.iloc[2:]

# df = df.drop(index=(range(2,10124)))




# 'Working code below'
# df = df.set_index(keys='Unnamed: 0',append=True) #indexing on date ...! => Does not do anything ?
# df = df.astype(np.float32) #force casting a variable to be a float

# df_pct = df.pct_change() #Making a new dataframe that consists of pct change 
# ### From the pct_change dataframe I am going to count all NaNs value => If they are more than one I am going to remove them from list ! 

# # print(df_pct.isna().sum().sort_values(ascending = False))
# df_pct_sorted = df_pct.dropna(axis='columns', how='any', thresh=2, subset=None, inplace=False)
# df = df_pct_sorted #Please undo me!!!!#
# print(df.iloc[2,[12]])
# print(df.iloc[2,[12]]) #okok litt progress .. må bare velge de bort nå 

# # print(df_pct_sorted.isna().sum().sort_values(ascending=True))

# # to_csv = pd.DataFrame.to_csv(df_pct_sorted,'C:\\Users\\march\\Desktop\\repo\\Trine\\Analysis\\test.csv')





# # acp_list = df['CloseXACPX'].tolist()
# # print(acp_list)


# # # print(df['CloseACP'].pct_change())

# '''Misc '''
