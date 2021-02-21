import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# Request data from MarketStack, you need to create an API account and get your key

params = {
  'access_key': 'your key here',
  'symbols': 'TSLA,AAPL,GOOGL,AMD,NVDA'
}

api_result = requests.get('http://api.marketstack.com/v1/intraday/latest', params)
api_response = api_result.json()

# Log to Google Auth, you need to create a credential file on google

scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'your key file here'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

i=0


# Save the requested data to the google sheet

sheet = client.open('google sheets file').worksheet('sheet1')
with open('marketstack.txt', 'w') as f:
  for stock_data in api_response['data']:
    i += 1
    price = str(stock_data['close'])
    strprice = price.replace(".", ",")
    print(stock_data['symbol'] + ' ' + strprice)
    f.write(stock_data['symbol'] + ' ' + strprice + '\n')
    sheet.update_cell(i, 1, stock_data['symbol'])
    sheet.update_cell(i, 2, strprice)



