import datetime

def format_date(date_str):
    """Convert a date string in the format 'YYYY-MM-DD' to a datetime object."""
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

def format_price(price):
    """Format the price to two decimal places."""
    try:
        return f"${float(price):,.2f}"
    except (ValueError, TypeError):
        return "$0.00"

import json

def parse_api_response(response):
    """
    Parse the API response and handle errors.

    Args:
        response (requests.Response): The API response object.

    Returns:
        tuple: (data, error) where `data` is the parsed JSON response and `error` is
               any error message encountered during parsing.
    """
    try:
        data = response.json()
        if 'Error Message' in data:
            return None, data['Error Message']
        return data, None
    except json.JSONDecodeError as e:
        return None, f"Error decoding JSON: {str(e)}"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"


def extract_stock_info(data):
    """Extract relevant stock information from the API response data."""
    if 'Time Series (5min)' in data:
        return {
            'price': data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]['4. close'],
            'high': data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]['2. high'],
            'low': data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]['3. low']
        }
    return None
