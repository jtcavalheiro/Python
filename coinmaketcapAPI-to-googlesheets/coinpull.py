from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# Request data from Coinmarketcap, you need to create an API account and get your key

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'BTC,ETH,BCH',
  'convert':'EUR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'your key here',
}
session = Session()
session.headers.update(headers)


# Log to Google Auth, you need to create a credential file on google

scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'your key file here'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

# Save the requested data to the google sheet

try:
  response = session.get(url, params=parameters)
  api_response = json.loads(response.text)

  i = 0
  sheet = client.open('googlesheetsfile').worksheet('sheet1')
  with open('files/coin.txt', 'w') as f:
    for coin_data in api_response['data'].keys():
      price = str(api_response['data'][coin_data]['quote']['EUR']['price'])
      strprice = price.replace(".", ",")
      print(coin_data, ' ', strprice)
      i += 1
      f.write(coin_data + ' ' + strprice + '\n')
      sheet.update_cell(i, 1, coin_data)
      sheet.update_cell(i, 2, strprice)


except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  