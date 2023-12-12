import streamlit as st
import requests

def get_crypto_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[coin]['usd']

def main():
    st.title("Crypto Price Checker")

    # Specify the cryptocurrencies you want to track
    cryptocurrencies = ["bitcoin", "ethereum", "litecoin"]

    selected_crypto = st.selectbox("Select a cryptocurrency", cryptocurrencies)

    price = get_crypto_price(selected_crypto)
    st.write(f"Current Price of {selected_crypto.capitalize()}: ${price}")

if __name__ == "__main__":
    main()
