import streamlit as st
import pandas as pd

portfolio = []

def display_portfolio():
    st.write("Add Stocks to your Portfolio")

    stock_symbol = st.text_input("Stock Symbol (e.g., AAPL)")
    quantity = st.number_input("Quantity", min_value=1, max_value=1000)

    if st.button("Add to Portfolio"):
        portfolio.append({'symbol': stock_symbol, 'quantity': quantity})
        st.success(f"Added {quantity} of {stock_symbol} to portfolio")

    if portfolio:
        st.subheader("Your Portfolio")
        df = pd.DataFrame(portfolio)
        st.dataframe(df)
