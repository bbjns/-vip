import pandas as pd

def max_drawdown():
    df = pd.read_csv("trades.csv")
    equity = df["余额"]
    max_balance = equity.cummax()
    dd = (equity - max_balance) / max_balance
    return round(dd.min() * 100, 2)
