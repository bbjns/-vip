import requests

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    data = requests.get(url).json()
    return float(data["price"])

def open_long(symbol, qty):
    print("开多:", symbol, qty)

def close_position(symbol):
    print("平仓:", symbol)
