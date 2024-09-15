import streamlit as st
from pages import stock_market

st.sidebar.title("KGI Task & Goal Management")
menu = st.sidebar.selectbox("Select Feature", ["Home", "Stock Market Tracker", "Portfolio", "Alerts"])

if menu == "Stock Market Tracker":
    stock_market.display_stock_market_tracker()
