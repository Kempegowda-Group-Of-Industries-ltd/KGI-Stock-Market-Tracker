import streamlit as st

alerts = {}

def display_alerts(symbol):
    target_price = st.number_input(f"Set Target Price for {symbol.upper()}", min_value=0.0)

    if st.button("Set Alert"):
        alerts[symbol] = target_price
        st.success(f"Alert set for {symbol.upper()} at {target_price}")
    
    if symbol in alerts:
        st.write(f"Current alert for {symbol.upper()}: {alerts[symbol]}")
