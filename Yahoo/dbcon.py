#Database writer - test 
import pyodbc
import pathlib

from pyparsing import str_type
 
msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
print('MS-Access Drivers : {msa_drivers}')

 #Checking wo i am, where i am ... 
path_string = str(pathlib.Path(__file__).parent.resolve()) 

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path_string + '/testdb.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")
    
except:
    pass

