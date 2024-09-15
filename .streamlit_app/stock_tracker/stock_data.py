import requests
import pandas as pd
from .utils import parse_api_response

API_KEY = 'YOUR_ALPHAVANTAGE_API_KEY'
BASE_URL = 'https://www.alphavantage.co/query'

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
        return pd.DataFrame(), error  # Return empty DataFrame and error
    
    if 'bestMatches' in data:
        # Convert to a DataFrame for better handling and display
        return pd.DataFrame(data['bestMatches']), None  # Return DataFrame and no error
    
    return pd.DataFrame(), "No matches found."  # Return empty DataFrame and message

def get_stock_data(symbol):
    """Get stock data for a given symbol."""
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data, error = parse_api_response(response)
    
    if error:
        return None, error  # Return None and error
    
    return data, None  # Return data and no error
