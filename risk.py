from config import RISK_PER_TRADE

def calc_position(price):
    balance = 1000
    risk_amount = balance * RISK_PER_TRADE
    qty = risk_amount / price
    return qty
