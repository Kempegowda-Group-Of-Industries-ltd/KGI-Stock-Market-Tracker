import requests
from .utils import format_price, parse_api_response

def get_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=7BJZMCBGIP1SHX23"
    response = requests.get(url)
    data, error = parse_api_response(response)

    if error:
        return None, error

    stock_info = extract_stock_info(data)
    return stock_info, None

def search_stock(query):
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={query}&apikey=7BJZMCBGIP1SHX23"
    response = requests.get(url)
    data, error = parse_api_response(response)

    if error:
        return None, error

    return data.get('bestMatches', []), None
