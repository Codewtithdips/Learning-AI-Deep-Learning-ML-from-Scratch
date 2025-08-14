import streamlit as st
import requests
import pandas as pd
import time

def fetch_stock_prices(symbol, api_key):
    """Fetches current stock prices from Finhub API"""
    url = f"https://api.finage.co.uk/last/stock/{symbol}?apikey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['ask']

st.set_page_config(page_title="Real-Time Stock Prices", layout="centered")
st.title("📈 Real-Time Stock Price Monitor")

api_key = "API_KEYfcRX7PLQ7Y114EPT13F1SQ1A1C6HSFBD"# Secure storage

symbols = st.multiselect("Select Stocks", ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"])

refresh_rate = st.slider("Refresh interval (seconds)", 5, 60, 10)

if symbols:
    placeholder = st.empty()

    while True:
        prices = []
        for symbol in symbols:
            try:
                price = fetch_stock_prices(symbol, api_key)
                prices.append({"Symbol": symbol, "Price": price if price else "N/A"})
            except Exception as e:
                prices.append({"Symbol": symbol, "Price": f"Error: {e}"})

        df = pd.DataFrame(prices)
        placeholder.table(df)

        time.sleep(refresh_rate)
