import streamlit as st
from stock_tracker import stock_data, portfolio, alerts
import plotly.express as px

def display_stock_market_tracker():
    st.title("📈 Stock Market Tracker")

    # Search for stocks
    search_query = st.text_input("Search Stock Market (Company Name, Symbol, etc.)", "")
    if search_query:
        search_results = stock_data.search_stock(search_query)
        if search_results:
            st.write(f"Search results for: {search_query}")
            st.dataframe(search_results)

    # Input for Stock Symbol
    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA)", "")
    if symbol:
        stock_info = stock_data.get_stock_data(symbol)

        if stock_info:
            # Display real-time stock data
            st.subheader(f"Real-time Price of {symbol.upper()}")
            st.write(f"Current Price: {stock_info['price']}")
            st.write(f"Day High: {stock_info['high']}, Day Low: {stock_info['low']}")

            # Plot stock trend using Plotly
            fig = px.line(stock_info['historical'], x='date', y='close', title=f"{symbol.upper()} Price Trend")
            st.plotly_chart(fig)

        # Portfolio section
        st.subheader("📊 Portfolio Management")
        portfolio.display_portfolio()

        # Alerts section
        st.subheader("🔔 Set Stock Alerts")
        alerts.display_alerts(symbol)
