#Datainserter demo ....!#
import pyodbc


con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\isak\Desktop\dbfolder\pydb.accdb;'
conn = pyodbc.connect(con_string)
cursor = conn.cursor()

my_input = ( #<= Generated at ... 
    
    (5, 'EMO', 200, 'no'),
    (6, 'NTG', 300, 'yes'),
    (7, 'SOR', 400, 'no'),
)
cursor.executemany('INSERT INTO Table1 VALUES (?,?,?,?)', my_input) #Note the ?,?.. are placeholders for no. of entries 
conn.commit()


