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

def parse_api_response(response):
    """Parse and validate the API response, returning data or an error message."""
    if response.status_code == 200:
        data = response.json()
        if 'Error Message' in data:
            return None, f"Error: {data['Error Message']}"
        return data, None
    else:
        return None, f"HTTP Error {response.status_code}: {response.reason}"

def extract_stock_info(data):
    """Extract relevant stock information from the API response data."""
    if 'Time Series (5min)' in data:
        return {
            'price': data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]['4. close'],
            'high': data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]['2. high'],
            'low': data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]['3. low']
        }
    return None
