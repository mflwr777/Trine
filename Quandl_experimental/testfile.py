import nasdaqdatalink as ndl 

ndl.ApiConfig.api_key = 'rKpAg-m7Sx4HAXVbnio7'
ndl.ApiConfig.verify_ssl = True
data = ndl.get_table(datatable_code='NFN/CEFMAIN' , ticker='TYG')
data_tickername = data['name']
print(data)
print(data_tickername)

''' Able to connect, get prompted back but with an empty dataset  => Premium service, have asked for a trial version ...!'''

