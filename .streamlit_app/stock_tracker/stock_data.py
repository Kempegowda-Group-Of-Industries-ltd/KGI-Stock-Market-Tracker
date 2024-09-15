import requests
import pandas as pd

API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

def get_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if 'Time Series (5min)' in data:
        historical = []
        for timestamp, details in data['Time Series (5min)'].items():
            historical.append({
                'date': timestamp,
                'open': details['1. open'],
                'high': details['2. high'],
                'low': details['3. low'],
                'close': details['4. close']
            })
        return {
            'price': historical[0]['close'],
            'high': historical[0]['high'],
            'low': historical[0]['low'],
            'historical': historical
        }
    return None

def search_stock(query):
    # Example of a simple stock search using Alpha Vantage
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={query}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if 'bestMatches' in data:
        # Convert search results into a DataFrame for easier display
        results = pd.DataFrame(data['bestMatches'])
        return results[['1. symbol', '2. name', '4. region', '8. currency']]
    return None
