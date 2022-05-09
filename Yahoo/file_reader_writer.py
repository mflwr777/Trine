from ntpath import join
from operator import index
from re import S
from numpy import append, dtype
from pyparsing import str_type
import yfinance
import config 
import pandas as pd
p = print

# Reading all cefs and converting them into a list 
cef_loader = pd.read_csv(r'C:\Users\isak\Desktop\working_folder\alpaca\Yahoo\ceflist.csv')['Symbol']
cef_prices = [cef_loader[n] for n in range(len(cef_loader.index))]
cef_navs = ['X' + cef_prices[n] + 'X' for n in range(len(cef_loader.index))]

print(cef_navs)




