' Documentation: https://pypi.org/project/yfinance/'
import imp
import pandas as pd 
import yfinance as yf
import numpy as np 
import requests 
import lxml
from functools import cache
from pandas import DataFrame as df

import file_reader_writer as frw

# Edit me if you want! 
tickerlist1 =  ["TYG", "NTG", "SOR", "NDP", "FEI", "EMO", "NML", "IGR", "RQI", "CHY", "CHI", "CCD"]
tickerlist2 = ['XACPX', 'XACVX', 'XADXX', 'XAEFX', 'XAFBX', 'XAFTX', 'XAGDX', 'XAIFX', 'XAIOX', 'XAODX', 'XARDCX', 'XASAX', 'XASGX', 'XASGIX', 'XAVKX', 'XAWFX', 'XAWPX', 'XBANXX', 'XBBNX', 'XBCATX', 'XBCVX', 'XBCXX', 'XBDJX', 'XBFKX', 'XBFZX', 'XBGBX', 'XBGHX', 'XBGRX', 'XBGTX', 'XBGXX', 'XBGYX', 'XBHKX', 'XBHVX', 'XBIFX', 'XBIGZX', 'XBITX', 'XBKNX', 'XBKTX', 'XBLEX', 'XBLWX', 'XBMEX', 'XBMEZX', 'XBNYX', 'XBOEX', 'XBRWX', 'XBSLX', 'XBSTX', 'XBSTZX', 'XBTAX', 'XBTOX', 'XBTTX', 'XBTZX', 'XBUIX', 'XBWGX', 'XBXMXX', 'XBYMX', 'XCAFX', 'XCBHX', 'XCCDX', 'XCEEX', 'XCEFX', 'XCEMX', 'XCENX', 'XCETX', 'XCEVX', 'XCGOX', 'XCHIX', 'XCHNX', 'XCHWX', 'XCHYX', 'XCIFX', 'XCIIX', 'XCIKX', 'XCLMX', 'XCMUX', 'XCPZX', 'XCRFX', 'XCSQX', 'XCTRX', 'XCUBAX', 'XCXEX', 'XCXHX', 'XDBLX', 'XDCFX', 'XDDFX', 'XDEXX', 'XDFPX', 'XDHFX', 'XDHYX', 'XDIAXX', 'XDLYX', 'XDMAX', 'XDMBX', 'XDMFX', 'XDMOX', 'XDNPX', 'XDPGX', 'XDSLX', 'XDSMX', 'XDSUX', 'XDTFX', 'XDYFNX', 'XEADX', 'XECATX', 'XECCX', 'XECFX', 'XEDDX', 'XEDFX', 'XEDIX', 'XEEAX', 'XEFLX', 'XEFRX', 'XEFTX', 'XEGFX', 'XEHIX', 'XEICX', 'XEIMX', 'XEMDX', 'XEMFX', 'XEMOX', 'XENXX', 'XEODX', 'XEOIX', 'XEOSX', 'XEOTX', 'XERCX', 'XERHX', 'XETBX', 'XETGX', 'XETJX', 'XETOX', 'XETVX', 'XETWX', 'XETXX', 'XETYX', 'XEVFX', 'XEVGX', 'XEVMX', 'XEVNX', 'XEVTX', 'XEVVX', 'XEXDX', 'XEXGX', 'XFAMX', 'XFAXX', 'XFCOX', 'XFCTX', 'XFDEUX', 'XFEIX', 'XFENX', 'XFEOX', 'XFFAX', 'XFFCX', 'XFGBX', 'XFIFX', 'XFINSX', 'XFLCX', 'XFMNX', 'XFMOX', 'XFMYX', 'XFOFX', 'XFPFX', 'XFPLX', 'XFRAX', 'XFSDX', 'XFTX', 'XFTFX', 'XFTHYX', 'XFUNDX', 'XGABX', 'XGAMX', 'XGBABX', 'XGCVX', 'XGDLX', 'XGDOX', 'XGDVX', 'XGERX', 'XGFX', 'XGGNX', 'XGGTX', 'XGGZX', 'XGHYX', 'XGIMX', 'XGLOX', 'XGLQX', 'XGLUX', 'XGLVX', 'XGNTX', 'XGOFX', 'XGRFX', 'XGRXX', 'XGUGX', 'XGUTX', 'XHEQX', 'XHFROX', 'XHGLBX', 'XHIEX', 'XHIOX', 'XHIXX', 'XHNWX', 'XHPFX', 'XHPIX', 'XHPSX', 'XHQHX', 'XHQLX', 'XHTDX', 'XHTYX', 'XHYBX', 'XHYIX', 'XHYTX', 'XIAEX', 'XIAFX', 'XIDEX', 'XIFNX', 'XIGAX', 'XIGDX', 'XIGIX', 'XIGRX', 'XIHDX', 'XIHITX', 'XIHTAX', 'XIIFX', 'XIIMX', 'XINSIX', 'XIQIX', 'XIRLX', 'XISDX', 'XIVHX', 'XJCEX', 'XJCOX', 'XJEMDX', 'XJEQX', 'XJFRX', 'XJGHX', 'XJHAAX', 'XJHIX', 'XJHSX', 'XJLSX', 'XJMMX', 'XJOFX', 'XJPCX', 'XJPIX', 'XJPSX', 'XJPTX', 'XJQCX', 'XJRIX', 'XJROX', 'XJRSX', 'XJSDX', 'XKFX', 'XKIOX', 'XKMFX', 'XKSMX', 'XKTFX', 'XKYNX', 'XLDPX', 'XLEOX', 'XLGIX', 'XMAVX', 'XMCAX', 'XMCIX', 'XMCNX', 'XMCRX', 'XMEGIX', 'XMFDX', 'XMFLX', 'XMFMX', 'XMFVX', 'XMGFX', 'XMGUX', 'XMHDX', 'XMHFX', 'XMHIX', 'XMHNX', 'XMINX', 'XMIOX', 'XMIYX', 'XMMDX', 'XMMTX', 'XMMUX', 'XMNPX', 'XMPAX', 'XMPVX', 'XMQTX', 'XMQYX', 'XMSDX', 'XMUAX', 'XMUCX', 'XMUEX', 'XMUIX', 'XMUJX', 'XMVFX', 'XMVTX', 'XMXEX', 'XMXFX', 'XMYCX', 'XMYDX', 'XMYIX', 'XMYJX', 'XMYNX', 'XNACX', 'XNADX', 'XNANX', 'XNAZX', 'XNBBX', 'XNBHX', 'XNBOX', 'XNBWX', 'XNBXGX', 'XNCAX', 'XNCVX', 'XNCZX', 'XNDMOX', 'XNDPX', 'XNEAX', 'XNEVX', 'XNFJX', 'XNHSX', 'XNIDX', 'XNIEX', 'XNIMX', 'XNIQX', 'XNKGX', 'XNKXX', 'XNMAIX', 'XNMCOX', 'XNMIX', 'XNMLX', 'XNMSX', 'XNMTX', 'XNMZX', 'XNNYX', 'XNOMX', 'XNPCTX', 'XNPFDX', 'XNPVX', 'XNQPX', 'XNRGXX', 'XNRKX', 'XNROX', 'XNSLX', 'XNTGX', 'XNUOX', 'XNUVX', 'XNUWX', 'XNVGX', 'XNXCX', 'XNXDTX', 'XNXJX', 'XNXNX', 'XNXPX', 'XNZFX', 'XOCCIX', 'XOIAX', 'XOPPX', 'XOXLCX', 'XPAIX', 'XPAXSX', 'XPCFX', 'XPCKX', 'XPCMX', 'XPCNX', 'XPCQX', 'XPDIX', 'XPDOX', 'XPDTX', 'XPEOX', 'XPFDX', 'XPFLX', 'XPFNX', 'XPFOX', 'XPGPX', 'XPGZX', 'XPHDX', 'XPHKX', 'XPHTX', 'XPHYSX', 'XPIMX', 'XPMFX', 'XPMLX', 'XPMMX', 'XPMOX', 'XPMXX', 'XPNFX', 'XPNIX', 'XPPTX', 'XPSFX', 'XPSLVX', 'XPTAX', 'XPTYX', 'XPYNX', 'XPZCX', 'XQQQXX', 'XRAX', 'XRCGX', 'XRCSX', 'XRFIX', 'XRFMX', 'XRFMZX', 'XRGTX', 'XRIVX', 'XRMIX', 'XRMMX', 'XRMMZX', 'XRMTX', 'XRNPX', 'XRQIX', 'XRSFX', 'XRVTX', 'XSBIX', 'XSCDX', 'XSDHYX', 'XSMMX', 'XSORX', 'XSPEX', 'XSPPPX', 'XSPXXX', 'XSRVX', 'XSSSSX', 'XSTKX', 'XSWZX', 'XSZCX', 'XTBLDX', 'XTDFX', 'XTEAFX', 'XTEIX', 'XTHQX', 'XTHWX', 'XTPZX', 'XTSIX', 'XTTPX', 'XTWNX', 'XTYX', 'XTYGX', 'XUSAX', 'XUTFX', 'XUTGX', 'XVBFX', 'XVCFX', 'XVCIFX', 'XVCVX', 'XVFLX', 'XVGIX', 'XVGMX', 'XVKIX', 'XVKQX', 'XVLTX', 'XVMMX', 'XVMOX', 'XVPVX', 'XVTNX', 'XVVRX', 'XWDIX', 'XWEAX', 'XWIAX', 'XWIWX', 'XXFLTX', 'XZTRX']
tickerlist3 = ['NTG','SOR']

single_tickerlist = ['NTG']
single_tickerlist2 = []

#'YYYY-MM-DD'
start_time = '2022-04-14' 
end_time = '2022-04-28'
time_period = None #Used if start_time, end_timne = None

# Do not edit me please 
yfinance_dict = {'periods':'[1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max','actions':'[info,actions,dividends,splits,financials,major_holders,institutional_holders,balance_sheet,cashflow,earnings,sustainability,recommendations,calendar,ISIN,options]'}


