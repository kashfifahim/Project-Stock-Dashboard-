import requests

API_KEY = 'Z26IND1A7LZTHK7V'

def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
    response = response.get(url)
    data = response.json()
    # Extract the lastest price from the JSON data
    latest_price = list(data['Time Series (5min)'].values())[0]['4. close']
    return latest_price