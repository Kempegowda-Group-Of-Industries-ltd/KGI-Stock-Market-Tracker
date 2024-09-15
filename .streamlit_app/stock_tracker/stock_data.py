import requests
import pandas as pd
from .utils import format_price, parse_api_response, extract_stock_info

API_KEY = '7BJZMCBGIP1SHX23'
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_data(symbol):
    """Fetch real-time stock data for a given symbol."""
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data, error = parse_api_response(response)
    
    if error:
        return None, error

    stock_info = extract_stock_info(data)
    if stock_info:
        stock_info['price'] = format_price(stock_info['price'])
        return stock_info, None
    return None, "No stock data available."

def search_stock(query):
    """Search for stocks based on a query."""
    params = {
        'function': 'SYMBOL_SEARCH',
        'keywords': query,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data, error = parse_api_response(response)
    
    if error:
        return None, error
    
    if 'bestMatches' in data:
        # Convert to a DataFrame for better handling and display
        return pd.DataFrame(data['bestMatches'])
    
    return pd.DataFrame(), "No matches found."

def extract_stock_info(data):
    """Extract relevant stock information from the API response data."""
    if 'Time Series (5min)' in data:
        latest_time = list(data['Time Series (5min)'].keys())[0]
        info = data['Time Series (5min)'][latest_time]
        return {
            'price': info['4. close'],
            'high': info['2. high'],
            'low': info['3. low']
        }
    return None
