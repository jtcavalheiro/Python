#   
#   Interact with Coinmarketcap API
#   https://coinmarketcap.com/api/
#
#   This script saves data to a google sheets file using gsheets.py
#   https://github.com/jtcavalheiro/Python/blob/master/gsheets.py
#

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from gsheets import savegsheet
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'BTC,ETH,BCH,XRP,FUEL,AAVE,MED,FUN,KICK,LINK,THETA',
  'convert':'EUR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'your key',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  api_response = json.loads(response.text)

  result = []

  for coin_data in api_response['data'].keys():
    
    price = str(api_response['data'][coin_data]['quote']['EUR']['price'])
    strprice = price.replace(".", ",")
    result.append([coin_data, strprice])

  savegsheet('db_update', 'CoinMarketcap', result)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  

