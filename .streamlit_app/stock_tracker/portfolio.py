import streamlit as st

def display_portfolio():
    st.write("Add Stocks to your Portfolio")

    stock_symbol = st.text_input("Stock Symbol (e.g., AAPL)")
    quantity = st.number_input("Quantity", min_value=1, max_value=1000)

    if st.button("Add to Portfolio"):
        if stock_symbol:
            st.success(f"Added {quantity} of {stock_symbol} to portfolio")

    # Dummy data for demonstration
    portfolio = [{"symbol": "AAPL", "quantity": 10}]
    if portfolio:
        st.subheader("Your Portfolio")
        st.write(portfolio)
    else:
        st.write("Your portfolio is empty.")
