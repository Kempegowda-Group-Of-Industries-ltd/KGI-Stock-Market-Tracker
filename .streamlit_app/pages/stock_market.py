import streamlit as st
import pandas as pd
import plotly.express as px
from stock_tracker import get_stock_data, search_stock

def display_stock_market_tracker():
    st.title("Stock Market Tracker")

    # Search for stocks
    search_query = st.text_input("Search for Stocks", "")
    if st.button("Search"):
        if search_query:
            search_results, error = search_stock(search_query)
            if error:
                st.error(error)
            elif not search_results.empty:
                st.write(f"Search results for: {search_query}")
                st.dataframe(search_results)
            else:
                st.write("No results found.")
        else:
            st.write("Please enter a search query.")

    # Input for Stock Symbol
    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA)", "")
    if symbol and st.button("Get Stock Data"):
        stock_data, error = get_stock_data(symbol)
        if error:
            st.error(error)
        elif stock_data:
            st.write(f"Stock data for {symbol}")

            # Display stock data in JSON format
            st.json(stock_data)

            # Visualize stock data (example: closing price over time)
            time_series = stock_data.get('Time Series (5min)', {})
            if time_series:
                df = pd.DataFrame(time_series).T
                df.index = pd.to_datetime(df.index)
                df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
                df['Close'] = pd.to_numeric(df['Close'])
                df = df.sort_index()  # Sort by date to ensure proper plotting

                fig = px.line(df, x=df.index, y='Close', title=f'{symbol} Closing Price Over Time')
                st.plotly_chart(fig)
            else:
                st.write("No time series data available for visualization.")
