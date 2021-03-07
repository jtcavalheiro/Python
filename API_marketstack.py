#   
#   Interact with MarketStack API
#   https://marketstack.com/
#
#   This script saves data to a google sheets file using gsheets.py
#   
#


from gsheets import savegsheet
import requests, json


params = {
    'access_key': 'your key',
    'symbols': 'TSLA,AAPL,GOOGL,AMD,NVDA'
}

api_result = requests.get('http://api.marketstack.com/v1/intraday/latest', params)
api_response = api_result.json()

result = []

for stock_data in api_response['data']:

    price = str(stock_data['close'])
    strprice = price.replace(".", ",")
    result.append([stock_data['symbol'], strprice])
    
savegsheet('db_update', 'MarketStack', result)

